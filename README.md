# JanusGraph legal documents

[![Build Status][travis-shield]][travis-link]

[travis-shield]: https://travis-ci.org/JanusGraph/legal.svg?branch=master
[travis-link]: https://travis-ci.org/JanusGraph/legal

Table of contents

* [Contributing](#contributing)
* [Creating a new repo](#creating-a-new-repo)
* [License](#license)

## Contributing

Before you can contribute to JanusGraph, please sign the Contributor License
Agreement (CLA). This is not a copyright *assignment*, it simply gives the
JanusGraph project the permission and license to use and redistribute your
contributions as part of the project.

* If you are an individual writing original source code and you're sure you own
  the intellectual property, then you'll need to sign an
  [individual CLA](JanusGraph_ICLA_1.0.pdf).

* If you work for a company or another organization that may have claim to
  intellectual property you may produce, and the organization wants to allow you
  to contribute your work, then an authorized representative of the organization
  will need to sign a [corporate CLA](JanusGraph_CCLA_1.0.pdf).

**IMPORTANT:** DO NOT submit a pull request to this repo to sign the CLA. At
this time, signing the CLA at this time involves filling out the ICLA or CCLA
paperwork, scanning it in, and sending it to janusgraph-cla@googlegroups.com .

Whether you sign the CCLA or the ICLA, for each contributor, please include:

* the full name
* your email address
* your GitHub user id

Be sure to also configure your local GitHub clone to match the name and email
address in your CLA. See [these
instructions](https://github.com/JanusGraph/janusgraph/blob/master/CONTRIBUTING.md#configure-your-repo-to-match-the-cla)
for details.

For now, the process is manual; in the future, we hope to have an electronic
method for CLA signatures which will be much easier to manage.

## Creating a new repo

To create a new repo, copy the starter set of files from the
[`new-repo`](new-repo) directory and modify the `README.md` accordingly.

Then, make sure the following steps are done to ensure automated CLA
verification:

* add @JanusGraph/bots as "writer" to each new repo
* add `cla: yes` and `cla: no`
  [labels](https://github.com/JanusGraph/legal/labels) - be sure to use the same
  colors for visual consistency

## License

This repo uses a combination of [Apache 2.0](APACHE-2.0.txt) and
[CC-BY-4.0](CC-BY-4.0.txt); see [`LICENSE.txt`](LICENSE.txt) for details.
