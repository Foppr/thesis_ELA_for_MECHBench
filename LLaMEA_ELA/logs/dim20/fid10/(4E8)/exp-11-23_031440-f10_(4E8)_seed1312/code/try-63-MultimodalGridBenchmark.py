import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Grid of global minima terms with proper dimension handling
        grid_minima = 0.0
        for i in range(self.dim):
            # Modified frequencies and coefficients for increased complexity
            grid_minima += 1.2 * np.sin(4 * np.pi * x[i] / 2.5) * np.cos(2.5 * np.pi * x[i] / 1.8)
            
        # Add enhanced sinusoidal interference terms for increased complexity
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Changed interaction frequencies and coefficients
                interference += 0.9 * np.sin(3 * np.pi * (x[i] + x[j])) * np.cos(1.5 * np.pi * (x[i] - x[j]))
        
        # Add a more complex noise term with multiple components including cubic terms
        noise = 0.04 * np.sum(np.sin(6 * x) + 0.8 * np.cos(4 * x) + 0.7 * np.sin(8 * x) + 0.3 * x**3)
        
        # Add a small cubic interaction term between dimensions for additional complexity
        cubic_interaction = 0.015 * np.sum(x**3)
        
        # Add a cross-term interaction with higher order nonlinearity
        cross_term = 0.02 * np.sum((x**2) * np.sin(x))
        
        return basin_term + grid_minima + interference + noise + cubic_interaction + cross_term