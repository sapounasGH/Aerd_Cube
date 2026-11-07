from stac_loader import StacLoader
import consts


def main():
    loader = StacLoader()
    
    query = loader.search(
        collections=[consts.DEFAULT_COLLECTION],
        bbox=consts.DEFAULT_BBOX,
        datetime=consts.DEFAULT_DATETIME
    )
    
    xx = loader.load(
        query=query,
        bands=consts.DEFAULT_BANDS
    )
    
    print(xx)


if __name__ == "__main__":
    main()



if __name__ == "__main__":
    main()