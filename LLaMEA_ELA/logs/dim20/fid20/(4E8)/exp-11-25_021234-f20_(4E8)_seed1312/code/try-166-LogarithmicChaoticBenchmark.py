import numpy as np

class LogarithmicChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Logarithmic barrier potentials with radial scaling and chaotic modulation
        r = np.sqrt(np.sum(x**2))
        if r == 0:
            f1 = 0.0
        else:
            f1 = np.log(1.0 + 0.5 * r) * (0.3 * r**2 + 0.7 * r**3)
            
        # Chaotic cosine interactions with dynamic amplitudes and frequencies
        f2 = 0.0
        for i in range(self.dim):
            amp = 1.2 + 0.3 * np.sin(0.3 * i + 0.2 * r)
            freq = 2.5 + 2.5 * np.cos(0.4 * i + 0.1 * r)
            f2 += amp * np.cos(freq * x[i]) * np.exp(-0.02 * x[i]**2)
            
        # Radial quadratic couplings with adaptive coefficients
        f3 = 0.0
        for i in range(self.dim):
            coeff = 0.6 + 0.4 * np.sin(0.2 * i + 0.1 * r)
            f3 += coeff * x[i]**2
            
        # Stochastic phase-modulated harmonic terms with dynamic scaling
        f4 = 0.0
        for i in range(self.dim):
            phase = np.random.uniform(0, 2*np.pi) + 0.3 * np.sin(0.2 * i)
            scale = 1.2 + 0.3 * np.cos(0.1 * i + 0.2 * r)
            f4 += scale * np.sin(x[i] + phase) * np.exp(-0.04 * x[i]**2)
            
        # Enhanced boundary penalty with logarithmic scaling and exponential decay
        f5 = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                penalty = 3.0 * np.log(1.0 - x[i]/5.0)**2
            else:
                penalty = 3.0 * np.log(1.0 + x[i]/5.0)**2
            f5 += penalty * np.exp(-0.05 * x[i]**2)
            
        # Cross-dimensional chaotic interaction terms with fractal-like structure
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.6 + 0.4 * np.cos(0.3 * (i - j) + 0.2 * r)
                f6 += coupling * np.cos(x[i] * x[j]) * np.exp(-0.03 * (x[i]**2 + x[j]**2))
                
        # Global irregularity through polynomial terms with chaotic coefficients
        f7 = 0.0
        for i in range(self.dim):
            coeff1 = 0.3 + 0.2 * np.cos(0.2 * i)
            coeff2 = 0.5 + 0.3 * np.sin(0.3 * i)
            coeff3 = 0.15 + 0.15 * np.cos(0.4 * i)
            f7 += coeff1 * x[i]**6 + coeff2 * x[i]**4 + coeff3 * x[i]**2
            
        return f1 + f2 + f3 + f4 + f5 + f6 + f7