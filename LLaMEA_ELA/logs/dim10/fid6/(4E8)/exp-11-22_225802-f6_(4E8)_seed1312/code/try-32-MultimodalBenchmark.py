import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Quadratic basin term - global minimum at origin
        basin = 0.1 * np.sum(x**2)
        
        # Multimodal periodic terms with multiple global minima and dynamic scaling
        periodic = 0.0
        for i in range(self.dim):
            # Enhanced sinusoidal interactions with varying frequencies
            freq1 = 2 * (i + 1)  # Varying frequencies
            freq2 = 3 * (i + 1)
            periodic += np.sin(freq1 * x[i]) * np.cos(freq2 * x[i])
            
        # Additional complex sinusoidal terms for increased landscape complexity
        additional = 0.0
        for i in range(self.dim):
            # Modified nonlinear terms with different exponents and coefficients
            additional += (0.8 * np.sin(4 * np.pi * x[i])**3 + 
                          0.6 * np.cos(3 * np.pi * x[i])**3 +
                          0.3 * np.sin(6 * np.pi * x[i])**2)
            
        # Cross-term interactions between dimensions to increase complexity
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Slight modification in interaction type and scaling
                cross_term += np.sin(0.7 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                
        return basin + 0.5 * periodic + additional + 0.4 * cross_term