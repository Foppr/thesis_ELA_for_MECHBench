import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like oscillatory terms with self-similarity
        fractal_term = 0.0
        for i in range(self.dim):
            # Use a base frequency that scales with dimension index
            freq = 2.0 + 0.5 * np.sin(i * 0.7)
            # Apply multiple sine waves with different amplitudes and frequencies
            fractal_term += (0.3 * np.sin(freq * x[i]) * 
                            np.cos(1.5 * freq * x[i]) * 
                            np.exp(-0.1 * np.abs(x[i])) + 
                            0.1 * np.sin(3 * freq * x[i]) * 
                            np.cos(2 * freq * x[i]))
        
        # Adaptive ridge structure with dimension-dependent scaling
        ridge_term = 0.0
        for i in range(self.dim):
            # Create a ridge-like structure that varies with dimension
            ridge_height = 0.5 * (1 + np.tanh(x[i] / (1.0 + i * 0.1)))
            ridge_term += ridge_height * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional interaction with fractal scaling
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction to avoid excessive computation
                # Use a distance-based scaling that mimics fractal behavior
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                scale_factor = 1.0 / (1.0 + dist**2)
                cross_term += scale_factor * np.sin(2 * x[i]) * np.cos(3 * x[j])
        
        # Scale-invariant global modulation
        global_mod = 0.0
        for i in range(self.dim):
            # Apply a combination of sinusoidal and polynomial scaling
            global_mod += 0.2 * (x[i]**3) * np.exp(-0.1 * np.abs(x[i])) * np.sin(0.5 * x[i])
        
        return fractal_term + ridge_term + cross_term + global_mod