# refsdomains
A short script to extract the most linked domains in references of a given Wikimedia site

This isn't meant to be pretty or optimized. It was a quick-and-dirty means to an end. [Standard disclaimer applies](https://xkcd.com/1513/).

## Usage

This is mostly for my own reference, but it might be useful in case I get hit by a bus.

* Obtain an [XML dump](https://dumps.wikimedia.org/backup-index-bydb.html) of the Wikimedia wiki you want to analyze. You want the `xxwiki*-2015xxxx-pages-articles*.xml*.bz2` file(s).
* Run the [mwrefs script](https://github.com/halfak/mwrefs) on it to extract the references. Example:
 * `nice ./utility extract frwiki-20150512-pages-articles?.xml.bz2 | bzip2 -c > mwrefs-frwiki-20150512.bz2`
* Extract the archive to a `.tsv` file, and run the script:
 * `./refsdomains.sh`
* The results are in the `sorted_domain_list.txt`.

## Background

This was done as part of a [short research project](https://meta.wikimedia.org/wiki/Research:Citoid_support_for_Wikimedia_references) looking into how well [Citoid](https://www.mediawiki.org/wiki/citoid) supported references commonly used on Wikimedia sites. 
