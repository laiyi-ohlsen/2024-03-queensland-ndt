query=f'''
WITH downloads AS (
SELECT
  client.Network.ASName as ASName,
  APPROX_QUANTILES(a.MeanThroughputMbps, 100)[OFFSET(50)] as median,
  COUNT(*) as testcount
FROM `measurement-lab.ndt_intermediate.extended_ndt7_downloads`
WHERE date >= "2024-01-01"
AND client.Geo.CountryCode = "AU"
AND client.Geo.Subdivision1Name = "Queensland"
AND client.Network.ASName IS NOT NULL
AND (filter.IsComplete -- Not missing any important fields
      AND filter.IsProduction -- not a test server
      AND NOT filter.IsError -- Server reported an error
      AND NOT filter.IsOAM -- operations and management traffic
      AND NOT filter.IsPlatformAnomaly -- overload, bad version, etc
      AND NOT filter.IsSmall -- less than 8kB data
      AND (NOT filter.IsShort OR filter.IsEarlyExit) -- insufficient duration or early exit.
      AND NOT filter.IsLong -- excessive duraton
      -- TODO(https://github.com/m-lab/k8s-support/issues/668) deprecate? _IsRFC1918
      AND NOT filter._IsRFC1918)
      GROUP BY ASName
),

uploads AS (
SELECT
  client.Network.ASName as ASName,
  APPROX_QUANTILES(a.MeanThroughputMbps, 100)[OFFSET(50)] as median,
  COUNT(*) as testcount
FROM `measurement-lab.ndt_intermediate.extended_ndt7_uploads`
WHERE date >= "2024-01-01"
AND client.Geo.CountryCode = "AU"
AND client.Geo.Subdivision1Name = "Queensland"
AND client.Network.ASName IS NOT NULL
AND (filter.IsComplete -- Not missing any important fields
      AND filter.IsProduction -- not a test server
      AND NOT filter.IsError -- Server reported an error
      AND NOT filter.IsOAM -- operations and management traffic
      AND NOT filter.IsPlatformAnomaly -- overload, bad version, etc
      AND NOT filter.IsSmall -- less than 8kB data
      AND (NOT filter.IsShort OR filter.IsEarlyExit) -- insufficient duration or early exit.
      AND NOT filter.IsLong -- excessive duraton
      -- TODO(https://github.com/m-lab/k8s-support/issues/668) deprecate? _IsRFC1918
      AND NOT filter._IsRFC1918)
      GROUP BY ASName
)

SELECT 
  downloads.ASName as ASName,
  ROUND(downloads.median, 2) as median_download, 
  ROUND(uploads.median, 2) as median_upload, 
  downloads.testcount as testcount
FROM downloads JOIN uploads ON downloads.ASName = uploads.ASName
ORDER BY testcount DESC
LIMIT 10
'''