import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Convert to numpy array and ensure correct shape
        x = np.array(x)
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Enhanced multimodal term with chaotic perturbations and dynamic conditioning
        multimodal = 0.0
        for i in range(self.dim):
            # Chaotic perturbation using sine and cosine with varying frequencies
            chaotic_term = np.sin(5 * np.pi * x[i]) * np.cos(7 * np.pi * x[i])
            
            # Exponential decay with dynamic conditioning based on dimension
            decay_factor = np.exp(-0.1 * (i + 1) * x[i]**2)
            
            # Polynomial interaction term
            poly_interaction = (x[i]**4 - 2*x[i]**2 + 1)
            
            # Combine all terms with dynamic scaling
            multimodal += decay_factor * chaotic_term * poly_interaction
            
        # Add a sinusoidal interference term to increase complexity
        interference = 0.5 * np.sum(np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x))
        
        # Add a small controlled noise term for reproducibility
        np.random.seed(hash(str(x)) % (2**32))
        noise = 0.005 * np.sum(np.random.rand() * np.abs(x))
        
        return basin_term + multimodal + interference + noise