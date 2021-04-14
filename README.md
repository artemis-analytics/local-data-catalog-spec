# Data Repository Specification


## Recommendation based on "Guidelines for a Standardized Filesystem Layout for Scientific Data"
[Guidelines for Standardized Filesystem Layout](https://www.mdpi.com/2306-5729/5/2/43/pdf)

- RawData
- ProcessedData
- SimulationData
- DataAnalysis
- Publications

Retain raw data files and metadata with URIs or metadata with URIs pouinting to source.    
`RawData\project_uuid_<ProjectName>\provider_uuid_<ProviderName>\<reference_period_datasetid>` 

Processed data is standardized format of raw data sources. May also include linked datasets in integrated table.    
`ProcessedData\project_uuid_<ProjectName>\provider_uuid_<ProviderName>\<reference_period_datasetid>` 

Data analysis includes integrated datasets from multiple sources and further improvements to processed data.  
`DataAnalysis\project_uuid_<ProjectName>\<reference_period_analysisid>`  

Publications include all data products, visualizations, papers, etc... anything that would go to a public repository.   
`Publications\project_uuid_<ProjectName>\<reference_period_productid>` 

Each directory contains a README.md file describing the contents of the dataset. See example README below.

Embedding additional metadata into the folder names can improve metadata while also supporting findable data.  
provider -> dcat:publisher  
uuid -> dcat:identifier   

## Metadata

Recommendation is to adopt DCAT vocabulary (or schema) as much as possible.

[Data Catalog Vocabulary (DCAT) Version 2](https://www.w3.org/TR/vocab-dcat-2/)

[Reference for DCAT in the US Federal gov, examples below] (https://resources.data.gov/resources/dcat-us/)

[Stat-DCAT Application Profile](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/solution/statdcat-application-profile-data-portals-europe)

Metadata - use dcat vocabulary (required and recommended where possible) along with yaml.
Just use the json or yaml fields and drop the JSON-LD components
Note that the JSON-LD has advantages such as namespacing, but currently lack capabalities to publish linked data.

Extend the schema to accomodate our use case for describing data assets in a standard file system layout. The intent to allow for metadata
to be harvested by data management systems (e.g. CKAN).

### Catalog Fields

**dataset**     
Dataset A container for the array of Dataset objects. See Dataset Fields below for details. Always.   
Example `{"dataset": [...]}`

### Dataset Fields

**title**     
Title Human-readable name of the asset. Should be in plain English and include sufficient detail to facilitate search and discovery. Always.   
Example `{"title":"Types of Vegetables"}` 

**description**  
Description Human-readable description (e.g., an abstract) with sufficient detail to enable a user to quickly understand whether the asset is of interest. Always.   
Example `{"description":"This dataset contains a list of vegetables, including nutrition information and seasonality. Includes details on tomatoes, which are really fruit but considered a vegetable in this dataset."}` 

**keyword**   
Tags Tags (or keywords) help users discover your dataset; please include terms that would be used by technical and non-technical users. Always.  
Example `{"keyword":["vegetables","veggies","greens","leafy","spinach","kale","nutrition"]}` 

**modified**   
Last Update Most recent date on which the dataset was changed, updated or modified. Always.   
Example `{"modified":"2012-01-15"}` ISO 8601 Date

**publisher**   
Publisher The publishing entity and optionally their parent organization(s). Always.  
<code>
	"publisher": {
	  "@type": "org:Organization",
	  "name": "Widget Services",
	  "subOrganizationOf": {
		"@type": "org:Organization",
		"name": "Office of Citizen Services and Innovative Technologies",
		"subOrganizationOf": {
		  "@type": "org:Organization",
		  "name": "General Services Administration",
		  "subOrganizationOf": {
			"@type": "org:Organization",
			"name": "U.S. Government"
		  }
		}
	  }
	}
</code>

**contactPoint**   
Contact Name and Email Contact person’s name and email for the asset. Always.   
 <code>
 "contactPoint": {
                "@type": "vcard:Contact",
                "fn": "Jane Doe",
                "hasEmail": "mailto:jane.doe@agency.gov"
            }
</code>
			

**identifier**   
Unique Identifier A unique identifier for the dataset or API as maintained within an Agency catalog or database. Always.  
Example `{"identifier":"http://dx.doi.org/10.7927/H4PZ56R2"}` 

**isPartOf**  
Collection The collection of which the dataset is a subset.  
`{"isPartOf":"http://dx.doi.org/10.7927/H4PZ56R2"}`

**accessLevel**  
Public Access Level The degree to which this dataset could be made publicly-available, regardless of whether it has been made available. Choices: public (Data asset is or could be made publicly available to all without restrictions), restricted public (Data asset is available under certain use restrictions), or non-public (Data asset is not available to members of the public).  
Example `{"accessLevel":"public"}` 

**rights**  
Rights This may include information regarding access or restrictions based on privacy, security, or other policies. This should also serve as an explanation for the selected “accessLevel” including instructions for how to access a restricted file, if applicable, or explanation for why a “non-public” or “restricted public” data asset is not “public,” if applicable. Text, 255 characters. If-Applicable 
URL to data sharing agreement.  
Example `{"rights":"This dataset contains Personally Identifiable Information and could not be released for public access."}` 

**spatial**  
Spatial The range of spatial applicability of a dataset. Could include a spatial region like a bounding box or a named place. If-Applicable 
Example `{"spatial":"Lincoln, Nebraska"}` 

**temporal**  
Temporal The range of temporal applicability of a dataset (i.e., a start and end date of applicability for the data). If-Applicable  
Example `{"temporal":"2000-01-15T00:45:00Z/2010-01-15T00:06:00Z"} or {"temporal":"2000-01-15T00:45:00Z/P1W"}` 
ISO 8601 Date

**distribution**  
Distribution A container for the array of Distribution objects. See Dataset Distribution Fields below for details. If-Applicable 
<code>
"distribution": [
                 {
                     "@type": "dcat:Distribution",
                     "description": "Vegetable data as a CSV file",
                     "downloadURL": "http://www.agency.gov/vegetables/listofvegetables.csv",
                     "format": "CSV",
                     "mediaType": "text/csv",
                     "title": "listofvegetables.csv"
                 }, 
                 {
                     "@type": "dcat:Distribution",
                     "conformsTo": "http://www.agency.gov/vegetables-data-standard/",
                     "describedBy": "http://www.agency.gov/vegetables/schema.xsd",
                     "describedByType": "text/xml",
                     "description": "Vegetable data as an XML file",
                     "downloadURL": "http://www.agency.gov/vegetables/listofvegetables.xml",
                     "format": "XML",
                     "mediaType": "text/xml",
                     "title": "listofvegetables.xml"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "description": "Vegetable data as a zipped CSV file with attached data dictionary",
                     "downloadURL": "http://www.agency.gov/vegetables/vegetables-all.zip",
                     "format": "Zipped CSV",
                     "mediaType": "application/zip",
                     "title": "vegetables-all.zip"
                 },
                 {
                     "@type": "dcat:Distribution",
                     "accessURL": "http://www.agency.gov/api/vegetables/",
                     "description": "A fully queryable REST API with JSON and XML output",
                     "format": "API",
                     "title": "Vegetables REST API"
                 }
                ]

				
				
</code>

**accrualPeriodicity**  
Frequency The frequency with which dataset is published. 
Example `{"accrualPeriodicity":"R/P1Y"}` 

**references**  
Related Documents Related documents such as technical information about a dataset, developer documentation, etc. No 
URL to additional documentation
Example `{"references":["http://www.agency.gov/legumes/legumes_data_documentation.html"]}` or if multiple URLs, `{"references":["http://www.agency.gov/legumes/legumes_data_documentation.html","http://www.agency.gov/fruits/fruit_data_documentation.html"]}` 

### Dataset Distribution

**description**  
Description Human-readable description of the distribution. No 

**downloadURL**  
Download URL URL providing direct access to a downloadable file of a dataset. If-Applicable 

**format**  
Format A human-readable description of the file format of a distribution. No 
Example `{"format":"CSV"}` 

**mediaType**  
Media Type The machine-readable file format (IANA Media Type or MIME Type) of the distribution’s downloadURL. If-Applicable 
Example `{"mediaType":"text/csv"}` 

**title**  
Title Human-readable name of the distribution. No 
Example `{"title":"listofvegetables.csv"}` 

**encoding**  
Codec codec of the distribution. Not part of the DCAT schema. 

stat:attribute
qb:AttributeProperty expressed as a URIs
A component used to qualify and interpret observed values. Enable specification of the units of measure, any scaling factores and metadata such as the status of operation
stat:dimension

stat:numSeries

stat:statUnitMeasure


## Example README.md for metadata

RawData example

```
---
title:
responsible:
- UserA
- UserB
publisher:
- Name
description:
sources:
- file:
  title:
  description:
  format:
  encoding:
  identifier
   
...
```

DataAnalysis example

```
---
title:
responsible:
description:
sources:
- <path_to_source_1>
- <path_to_source_2>
- ...
results:
- file:
  title:
  description:
  format:
  encoding:
  identifier:
- file:
  description:
  title:
  format:
  encoding:
  identifier:
scripts:
- file: <repository url>
```
