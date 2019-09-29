[![Contributors][contributors-shield]][contributors-url]
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors)
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<br />
<p align="center">
  <h1 align="center">Python-BPlusTree</h3>

  <p align="center">
    A simple and functional B+ Tree illustration & Visualization using
    <br>
    Python & <b>GraphViz</b>
  </p>
</p>

## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
  - [Built with](#built-with)
- [Getting Started](#getting-started)
  - [Usage](#usage)
    - [Without Visualization/Graphviz](#without-visualizationgraphviz)
    - [With Visualization](#with-visualization)
- [Contributing ✨](#contributing-%e2%9c%a8)
- [Authors](#authors)
- [License](#license)
- [Disclaimer](#disclaimer)
- [Security](#security)
- [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->

## About The Project

This B+ Tree implementation was created as part of an assignment for the University subject **Databases II** on the 5th Semester of [CS Dept., University of Thessaly][CSUTH].

It is free to use under MIT license and anyone wanting to can experiment and improve upon our implementation.

You can read more about B+ Trees [here](https://en.wikipedia.org/wiki/B%2B_tree).

### Built with
 - [Python 3](https://www.python.org/download/releases/3.0/)
 - [GraphViz](https://pypi.org/project/graphviz/)
 - And an uncountable amount of love :heart:
 


<!-- GETTING STARTED -->

## Getting Started

After making sure you have **installed any and all dependencies**, you can verify that our implementation is working by executing the following command:
    
    python bplustree.py

If you are planning to also Visualize the tree, give it a quick test by typing:

    python bplustree_with_visualizer.py

And that's it!



<!-- Usage -->

### Usage
#### Without Visualization/Graphviz
1. Import **BPlusTree** from `bplustree`.
2. Initialize BPlusTree
    ```
    bplustree = BPlusTree(order=5)
    ```
3. Insert/Delete by calling **bplustree.insert(key, value)** or **bplustree.delete(key)** accordingly, example:
    ```
    bplustree.insert(2, 'Bravo')
    bplustree.insert(13, 'November')
    bplustree.delete(2)
    ```
4. Call **bplustree.show_bfs()** to print the tree's in console.
5. Call **bplustree.show_all_data()** to print all data stored in the Leafs of the B+ Tree.

#### With Visualization
1. Import **GraphableBPlusTree** from `bplustree`.
2. You can use all the methods from above.
3. Call **bplustree.view_graph()** to generate a .png containing the B+ Tree.



<!-- Contributing -->

## Contributing ✨

Please read [CONTRIBUTING.md][CONTRIBUTING] for details on our code of conduct, and the process for submitting pull requests to us.

Thanks goes to these wonderful people who contribute✨:
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
> Life is not accumulation, it is about contribution. - Stephen Covey
> 
> I guess this ain't life. - WckdAwe
<!-- ALL-CONTRIBUTORS-LIST:END -->



<!-- Authors -->

## Authors
- **Dimitriadis Vasileios** (WckdAwe) --  ( [Website]( http://wckdawe.com) | [Github](https://github.com/wckdawe) )
- **Kouskouras Taxiarchis** (TheNotoriousCS) -- ( [Github](https://github.com/TheNotoriousCS) )



<!-- License -->

## License

This project is licensed under the MIT License - see the [LICENSE.md][LICENSE] file for details. 



<!-- Disclaimer -->

## Disclaimer

All the information on this repository is provided in good faith, however we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability or completeness of any information - see the [DISCLAIMER.md][DISCLAIMER] file for more details.



<!-- Security -->

## Security

For security related issues please read [SECURITY.md][SECURITY].



<!-- ACKNOWLEDGEMENTS -->

## Acknowledgements

Hats off to any person whom contributed to this Project, formally or informally. This couldn't be possible without the assistance of these people.

 - [Wikipedia](https://en.wikipedia.org/wiki/B%2B_tree)
 - [Javapoint](https://www.javatpoint.com/b-plus-tree)
 - [Stanford](https://web.stanford.edu/class/cs346/2015/notes/Blink.pptx)
 - [B+ Tree implementation by Savarin](https://gist.github.com/savarin/69acd246302567395f65ad6b97ee503d)
 - [B+ Tree implementation by pschafhalter](https://github.com/pschafhalter/python-b-plus-tree)
 - [B+ Tree implementation by cburch.com](http://www.cburch.com/cs/340/reading/btree/)

We have borrowed a-freaking-lot of ideas & code from the above guys to make our stuff kinda work. Make sure to check their individual projects out! :heart:










<!-- Github related links -->
[CONTRIBUTING]: https://github.com/WckdAwe/Python-BPlusTree/blob/master/CONTRIBUTING.md
[SECURITY]: https://github.com/WckdAwe/Python-BPlusTree/blob/master/SECURITY.md
[LICENSE]: https://github.com/WckdAwe/Python-BPlusTree/blob/master/LICENSE.md
[DISCLAIMER]: https://github.com/WckdAwe/Python-BPlusTree/blob/master/DISCLAIMER.md


<!-- othneildrew's Best-README-Template -->
[contributors-shield]: https://img.shields.io/github/contributors/WckdAwe/Python-BPlusTree.svg?style=flat-square
[contributors-url]: https://github.com/WckdAwe/Python-BPlusTree/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/WckdAwe/Python-BPlusTree.svg?style=flat-square
[forks-url]: https://github.com/WckdAwe/Python-BPlusTree/network/members
[stars-shield]: https://img.shields.io/github/stars/WckdAwe/Python-BPlusTree.svg?style=flat-square
[stars-url]: https://github.com/WckdAwe/Python-BPlusTree/stargazers
[issues-shield]: https://img.shields.io/github/issues/WckdAwe/Python-BPlusTree.svg?style=flat-square
[issues-url]: https://github.com/WckdAwe/Python-BPlusTree/issues
[license-shield]: https://img.shields.io/github/license/WckdAwe/Python-BPlusTree.svg?style=flat-square
[license-url]: https://github.com/WckdAwe/Python-BPlusTree/blob/master/LICENSE.md