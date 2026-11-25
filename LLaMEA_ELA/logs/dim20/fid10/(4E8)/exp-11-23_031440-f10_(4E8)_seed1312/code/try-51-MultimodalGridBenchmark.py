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
            # Create periodic pattern with multiple local minima using sine and cosine
            grid_minima += np.sin(3 * np.pi * x[i] / 2.0) * np.cos(3 * np.pi * x[i] / 1.5)
            
        # Add enhanced sinusoidal interference terms for increased complexity
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += 0.5 * np.sin(2 * np.pi * (x[i] + x[j])) * np.cos(2 * np.pi * (x[i] - x[j]))
        
        # Add a more complex noise term with multiple components
        noise = 0.02 * np.sum(np.sin(5 * x) + np.cos(3 * x) + 0.5 * np.sin(7 * x))
        
        # Enhanced multimodal component with higher frequency interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.3 * (np.sin(4 * np.pi * x[i]) + np.cos(2 * np.pi * x[i])) * np.exp(-0.1 * x[i]**2)
            
        # Cross-term interactions to increase conditioning difficulty
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.2 * (x[i]**2 + x[j]**2) * np.sin(0.5 * np.pi * (x[i] - x[j]))
        
        return basin_term + grid_minima + interference + noise + multimodal + cross_terms