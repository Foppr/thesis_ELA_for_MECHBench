import numpy as np

class ChaoticOscillatorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute frequency ratios for chaotic behavior
        self.freq_ratios = np.array([np.sqrt(i + 1) for i in range(dim)])
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) / self.dim
        
        # Coupled oscillator terms with time-varying coupling
        f2 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Dynamic coupling strength based on neighbor values and chaotic scaling
            coupling = 0.0
            if i > 0:
                coupling += 0.5 * np.sin(1.5 * (xi - x[i-1]))
            if i < self.dim - 1:
                coupling += 0.5 * np.sin(1.5 * (xi - x[i+1]))
            
            # Chaotic oscillator with varying frequency and amplitude
            freq = self.freq_ratios[i] * (1.0 + 0.3 * np.sin(xi))
            f2 += (np.sin(freq * xi + coupling) * np.cos(freq * xi**1.5))**2
        
        # Multi-scale sinusoidal modulation with fractal-like scaling
        f3 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple frequency components with decreasing amplitudes
            for k in range(1, 6):
                amp = 1.0 / (k * k)
                freq = k * self.freq_ratios[i] * (1.0 + 0.2 * np.cos(xi))
                f3 += amp * np.sin(freq * xi) * np.cos(freq * xi**0.7)
        
        # Asymmetric saddle points with varying curvature
        f4 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric cubic term with exponential weighting
            f4 += (xi**3 + 0.5 * xi**2 - 0.3 * xi) * np.exp(-0.1 * abs(xi))
        
        # Cross-term interaction with non-uniform coupling weights
        f5 = 0.0
        for i in range(self.dim - 1):
            xi, xj = x[i], x[i+1]
            # Nonlinear interaction with varying coupling strength
            coupling_strength = 0.3 * (1.0 + np.sin(0.5 * (xi + xj)))
            f5 += coupling_strength * np.sin(xi + xj) * np.cos(0.7 * xi - 0.3 * xj)
        
        # Fractional Brownian motion-like roughness with varying Hurst parameter
        f6 = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Fractional power with sinusoidal modulation
            f6 += (np.abs(xi)**1.3) * np.sin(15.0 * xi) * np.exp(-0.2 * abs(xi))
        
        # Combine all components with adjusted weights
        return 0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.05 * f6