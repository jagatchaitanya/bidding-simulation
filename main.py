from data.load_data import load_data
#from utils.preprocess import preprocess_data
from models.fit_curve import fit_curve
from models.model import gammafun
from utils.plot import plot_data_and_fit

def main():
    # Load data
    data = load_data('/Users/jagatchaitanya/Desktop/vishruti/bidding-simulation/data/FPSBA_merged.xlsx')
    
    # Preprocess data
    #data = preprocess_data(data)
    
    # Fit curve
    x_data = data['value']
    y_data = data['price_bid']
    popt, _ = fit_curve(x_data, y_data)
    
    # Plot results
    plot_data_and_fit(x_data, y_data, popt, gammafun)
    fout = open("alphavalue.txt","w")
    fout.write("optimalalpha is:"+str(popt))
    fout.close()

if __name__ == "__main__":
    main()
