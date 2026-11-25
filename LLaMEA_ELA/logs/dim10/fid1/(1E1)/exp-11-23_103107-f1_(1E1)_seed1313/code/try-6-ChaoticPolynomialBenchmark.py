import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Fractional polynomial basin term with non-integer exponents
        poly_basin = 0.005 * np.sum(np.abs(x)**3.5) + 0.05 * np.sum(np.abs(x)**1.7)
        
        # Chaotic sinusoidal terms with exponential modulation
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(15 * x[i]) * np.cos(11 * x[i]) * np.sin(8 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
        # Cross-term interactions with exponential decay
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Additional harmonic components with fractional frequencies
        harmonics = 0
        for i in range(self.dim):
            harmonics += np.sin(7 * x[i]**2.5) * np.cos(3 * x[i]**1.8) * np.exp(-0.02 * np.abs(x[i]))
            
        # Fractional power coupling terms creating ultra-narrow valleys
        fractional_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                fractional_coupling += (x[i]**0.7) * (x[j]**1.3) * np.sin(5 * (x[i] + x[j]))
                
        return poly_basin + chaotic + cross_terms + harmonics + fractional_coupling