import pystac_client
import odc.stac

def main():
    catalog = pystac_client.Client.open("https://earth-search.aws.element84.com/v1")
    query = catalog.search(
                collections=["sentinel-2-l2a"],
                bbox=[10, 50, 11, 51],
                datetime="2023-01-01/2023-01-31"
            )

    xx = odc.stac.load(
            query.items(),
            bands=["red", "green", "blue"]
        )

    print(xx.isnull)



if __name__ == "__main__":
    main()