import numpy as np

class AdaptiveFrequencyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial component with enhanced chaotic modulation
        r = np.sqrt(np.sum(x**2))
        freq_rad = 1.5 + 0.8 * np.sin(r / 3.0) * np.cos(r / 2.0)
        result += freq_rad * np.sin(4.0 * r) * np.cos(3.0 * r) * np.exp(-r/12.0)
        
        # Multi-frequency sinusoidal terms with dynamic coefficients
        for i in range(self.dim):
            xi = x[i]
            freq1 = 2.5 + 1.2 * np.sin(0.4 * i + r / 6.0)
            freq2 = 2.0 + 1.0 * np.cos(0.5 * i + r / 5.0)
            result += 0.8 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.3 * np.sin(6.0 * xi))
            
        # Enhanced polynomial coupling with radial dependency
        for i in range(self.dim):
            xi = x[i]
            result += 0.5 * (xi**4 - 2*xi**2 + 1) * np.exp(-r/8.0)
            
        # Improved harmonic interference with dynamic amplitudes
        for i in range(self.dim):
            xi = x[i]
            amp = 0.6 + 0.4 * np.sin(0.6 * i + r / 4.0)
            result += amp * np.sin(9.0 * xi + 0.5 * r) * np.cos(7.0 * xi + 0.4 * r)
            
        # Enhanced cross-dimensional coupling with variable decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                decay = 1.0 / (1.0 + 0.3 * np.abs(xi - xj))
                result += 0.4 * np.sin(xi + xj) * np.cos(xi - xj) * decay
                
        # Refined adaptive polynomial structure
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 3*xi**4 + 3*xi**2 - 1
            result += 0.3 * poly_term * np.exp(-xi**2/5.0)
            
        # Enhanced radial symmetry with frequency modulation
        result += 0.6 * r**2 * np.sin(5.0 * r + 0.6 * self.dim) * np.cos(4.0 * r + 0.4 * self.dim)
        
        # Additional high-frequency component with improved amplitude control
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * np.sin(18.0 * xi) * np.cos(12.0 * xi) * (1.0 + 0.2 * np.sin(r / 3.0))
            
        # Multi-scale coupling with optimized strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                strength = 0.25 + 0.15 * np.sin(0.3 * i + 0.4 * j + r / 5.0)
                result += strength * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/6.0)
                
        # Enhanced chaotic-like perturbation
        chaos_pert = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod = 1.2 + 0.4 * np.sin(0.8 * i + r / 7.0)
            chaos_pert += 0.3 * np.sin(freq_mod * xi + 2.5 * r) * np.cos(freq_mod * xi - 1.5 * r)
        result += chaos_pert * np.exp(-r/20.0)
        
        return result