import numpy as np

class NestedHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Nested harmonic oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            xi = x[i]
            # Multi-scale harmonic components with nested frequencies
            harmonic_sum = 0.0
            for k in range(1, 6):
                freq = k * (1.0 + 0.2 * np.sin(0.5 * i))
                amp = 1.0 / (k * (1.0 + 0.1 * np.cos(0.3 * i)))
                harmonic_sum += amp * np.sin(freq * xi)
            result += harmonic_sum**2
            
        # Fractional polynomial interactions with dynamic exponents
        for i in range(self.dim):
            xi = x[i]
            # Dynamic fractional exponent based on dimension and input value
            exp = 2.0 + 0.5 * np.sin(0.4 * i) * np.cos(0.3 * xi)
            result += (xi**exp) * (1.0 + 0.3 * np.sin(2.0 * xi))
            
        # Dynamic gradient modulation with coupling terms
        for i in range(self.dim):
            xi = x[i]
            # Coupling strength varies with dimension and input
            coupling = 1.0 + 0.4 * np.cos(0.5 * i) * np.sin(0.3 * xi)
            result += coupling * xi * np.cos(3.0 * xi)
            
        # Nested saddle point structure with rational polynomial components
        for i in range(self.dim):
            xi = x[i]
            # Rational polynomial that creates nested saddle points
            numerator = xi**3 - 2 * xi**2 + xi
            denominator = xi**2 + 0.5 + 0.2 * np.sin(4.0 * xi)
            if abs(denominator) > 1e-10:
                result += 0.5 * (numerator / denominator)**2
                
        # Multi-scale chaotic modulation with exponential decay
        for i in range(self.dim):
            xi = x[i]
            # Chaotic modulation with exponentially decaying influence
            modulator = np.exp(-0.1 * i) * (1.0 + 0.3 * np.sin(5.0 * xi))
            result += modulator * np.sin(7.0 * xi) * np.cos(2.0 * xi)
            
        # Add fractional polynomial coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractional coupling with dynamic exponent
                exp = 0.5 + 0.3 * np.sin(0.2 * (i + j))
                coupling = 1.0 + 0.2 * np.cos(0.3 * i) * np.sin(0.4 * j)
                result += coupling * (x[i]**exp) * (x[j]**(2.0 - exp))
                
        # Add multi-modal structure with nested peaks
        for i in range(self.dim):
            xi = x[i]
            # Nested peaks at different locations with varying heights
            peak1 = 1.0 / (1.0 + (xi - 3.0)**2 + 0.1 * np.sin(5.0 * xi))
            peak2 = 1.0 / (1.0 + (xi + 3.0)**2 + 0.1 * np.cos(4.0 * xi))
            peak3 = 1.0 / (1.0 + (xi - 1.0)**2 + 0.05 * np.tan(3.0 * xi))
            result += 0.8 * (peak1 + peak2 + peak3)
            
        # Add dynamic penalty near global optimum
        result += 0.6 * np.sum(np.exp(-0.3 * (x - 2.0)**2)) + 0.4 * np.sum(np.abs(x - 2.0)**3)
        
        return result