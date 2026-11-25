import numpy as np

class HarmonicPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add separable harmonic components with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Use harmonic oscillations with chaotic amplitude modulation
            amplitude = 2.0 + 1.5 * np.sin(0.3 * i)
            frequency = 1.0 + 0.8 * np.cos(0.4 * i)
            result += amplitude * np.sin(frequency * xi) * np.exp(-0.1 * xi**2)
            
        # Add polynomial chaos terms with dimension-dependent coefficients
        for i in range(self.dim):
            xi = x[i]
            # Use chaotic polynomial coefficients that vary with dimension index
            coeff = 1.0 + 0.5 * np.sin(0.6 * i)
            result += coeff * (xi**4 - 2.0 * xi**2 + 0.5) * np.exp(-0.3 * xi**2)
            
        # Add cross-dimensional coupling with harmonic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Adaptive coupling strength based on dimension indices and chaotic modulation
                coupling = 0.8 + 0.6 * np.sin(0.5 * (i - j))
                result += coupling * np.sin(2.0 * (x[i] + x[j])) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
                
        # Add superimposed higher-order polynomial terms with chaotic coefficients
        for i in range(self.dim):
            xi = x[i]
            coeff = 1.2 + 0.8 * np.cos(0.7 * i)
            result += coeff * (xi**6 - 4.0 * xi**4 + 4.0 * xi**2 - 1.0) * np.exp(-0.25 * xi**2)
            
        # Add chaotic conditioning with exponential scaling
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += np.exp(0.5 * x[i]**2) * np.sin(3.0 * x[i])
        result += 0.5 * conditioning
        
        # Add adaptive scaling based on global statistics with chaotic modulation
        mean_x = np.mean(x)
        std_x = np.std(x)
        chaos_factor = 1.0 + 0.5 * np.sin(0.8 * np.sum(x))
        result += chaos_factor * (std_x**3 + mean_x**3) * np.cos(1.5 * np.sum(x))
        
        # Add multi-dimensional chaotic interaction terms
        if self.dim >= 4:
            for i in range(self.dim - 3):
                # Quadruple-wise interactions with chaotic coupling
                result += 0.7 * np.sin(x[i] + x[i+1] + x[i+2] + x[i+3]) * np.cos(0.6 * (x[i]**2 + x[i+1]**2))
                
        # Add periodic penalty near the global optimum to increase convergence difficulty
        result += 0.4 * np.sum(np.sin(5.0 * (x - 1.0))**2)
        
        # Add chaotic frequency modulation in cross-dimensional terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_mod = 1.5 + 0.5 * np.sin(0.9 * (i + j))
                result += 0.3 * np.cos(freq_mod * (x[i] * x[j])) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Add additional chaotic oscillation component
        if self.dim > 1:
            oscillation = 0.0
            for i in range(self.dim):
                oscillation += np.cos(4.0 * x[i]) * np.sin(0.7 * i)
            result += 0.6 * oscillation * np.exp(-0.2 * np.sum(x**2))
            
        return result