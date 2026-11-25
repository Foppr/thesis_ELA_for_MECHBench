import numpy as np

class AdaptiveFrequencyBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.clip(x, -5.0, 5.0)
        result = 0.0
        
        # Radial component with adaptive frequency
        r = np.sqrt(np.sum(x**2))
        freq_rad = 1.0 + 0.5 * np.sin(r / 2.0)
        result += freq_rad * np.sin(3.0 * r) * np.cos(2.0 * r) * np.exp(-r/10.0)
        
        # Multi-frequency sinusoidal terms with adaptive coefficients
        for i in range(self.dim):
            xi = x[i]
            freq1 = 2.0 + 1.0 * np.sin(0.3 * i + r / 5.0)
            freq2 = 1.5 + 0.8 * np.cos(0.4 * i + r / 4.0)
            result += 0.7 * np.sin(freq1 * xi) * np.cos(freq2 * xi) * (1.0 + 0.2 * np.sin(5.0 * xi))
            
        # Polynomial coupling with radial dependency
        for i in range(self.dim):
            xi = x[i]
            result += 0.4 * (xi**4 - 2*xi**2 + 1) * np.exp(-r/6.0)
            
        # Harmonic interference with adaptive amplitudes
        for i in range(self.dim):
            xi = x[i]
            amp = 0.5 + 0.3 * np.sin(0.5 * i + r / 3.0)
            result += amp * np.sin(8.0 * xi + 0.4 * r) * np.cos(6.0 * xi + 0.3 * r)
            
        # Cross-dimensional coupling with adaptive decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                decay = 1.0 / (1.0 + 0.2 * np.abs(xi - xj))
                result += 0.3 * np.sin(xi + xj) * np.cos(xi - xj) * decay
                
        # Adaptive polynomial structure
        for i in range(self.dim):
            xi = x[i]
            poly_term = xi**6 - 3*xi**4 + 3*xi**2 - 1
            result += 0.25 * poly_term * np.exp(-xi**2/4.0)
            
        # Radial symmetry with frequency modulation
        result += 0.5 * r**2 * np.sin(4.0 * r + 0.5 * self.dim) * np.cos(3.0 * r + 0.3 * self.dim)
        
        # Additional high-frequency component with dynamic amplitude
        for i in range(self.dim):
            xi = x[i]
            result += 0.3 * np.sin(15.0 * xi) * np.cos(10.0 * xi) * (1.0 + 0.1 * np.sin(r / 2.0))
            
        # Multi-scale coupling with varying strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                xi = x[i]
                xj = x[j]
                strength = 0.2 + 0.1 * np.sin(0.2 * i + 0.3 * j + r / 4.0)
                result += strength * np.sin(xi + xj) * np.cos(xi - xj) * np.exp(-abs(xi-xj)/5.0)
                
        # Adaptive chaotic-like perturbation
        chaos_pert = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq_mod = 1.0 + 0.3 * np.sin(0.7 * i + r / 6.0)
            chaos_pert += 0.2 * np.sin(freq_mod * xi + 2.0 * r) * np.cos(freq_mod * xi - r)
        result += chaos_pert * np.exp(-r/15.0)
        
        return result