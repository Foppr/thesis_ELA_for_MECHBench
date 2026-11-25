import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = 0.1 * np.sum(x**2)
        
        # Add multiple sinusoidal wells with varying frequencies and amplitudes
        for i in range(1, min(self.dim + 1, 8)):
            # Create a well at position determined by a sinusoidal function
            well_x = 3.0 * np.sin(i * 0.5) * np.cos(i * 0.3)
            well_y = 3.0 * np.cos(i * 0.5) * np.sin(i * 0.3)
            
            # Calculate distance from well center
            if i <= 2 and self.dim >= 2:
                dist = np.sqrt((x[0] - well_x)**2 + (x[1] - well_y)**2)
                # Add sinusoidal well with varying depth
                result += 5.0 * np.sin(dist * i * 0.8) * np.exp(-dist**2 / (2 * (i * 0.5)**2))
            elif i <= self.dim:
                # For higher dimensions, use simpler sinusoidal terms
                result += 3.0 * np.sin(x[i-1] * i * 0.6) * np.exp(-abs(x[i-1] - well_x)**2 / (2 * (i * 0.4)**2))
        
        # Add radial barrier terms to create complex fitness landscape
        radial_dist = np.sqrt(np.sum(x**2))
        result += 2.0 * np.sin(radial_dist * 2.0) * np.exp(-radial_dist**2 / 50.0)
        
        # Add higher-order polynomial terms for increased complexity
        for i in range(self.dim):
            result += 0.2 * x[i]**6 - 1.2 * x[i]**4 + 0.8 * x[i]**2
        
        # Add noise component to increase ruggedness but reduce overall impact
        noise = 0.03 * np.sum(np.sin(10 * x))
        
        return result + noise