import numpy as np

class MultimodalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.sigma = 0.5
        self.k = 3.0
        
    def f(self, x):
        # Handle dimension mismatch
        if len(x) < self.dim:
            raise ValueError("Dimension mismatch: input has fewer dimensions than expected")
        elif len(x) > self.dim:
            x = x[:self.dim]
        
        # Scale input to [-5, 5] range if needed
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term - encourages convergence to origin
        radial_term = 0.1 * np.sum(x**2)
        
        # Multimodal sinusoidal components - creates multiple local minima
        modal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple sine waves with different frequencies and amplitudes
            modal_term += (np.sin(self.k * xi) + 
                          0.5 * np.sin(2 * self.k * xi) + 
                          0.3 * np.sin(3 * self.k * xi)) * np.exp(-0.1 * xi**2)
        
        # Cross-dimensional interaction terms - creates non-separability
        interaction_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction based on distance and angle between dimensions
                dist = np.sqrt((x[i] - x[j])**2 + (x[i] + x[j])**2)
                angle = np.arctan2(x[j], x[i])
                interaction_term += np.sin(dist) * np.cos(angle) * (i + j)
        
        # Add noise-like perturbation for increased complexity
        noise_term = 0.05 * np.sum(np.sin(x * self.sigma))
        
        # Combine all terms with proper scaling
        return radial_term + 0.3 * modal_term + 0.1 * interaction_term + noise_term