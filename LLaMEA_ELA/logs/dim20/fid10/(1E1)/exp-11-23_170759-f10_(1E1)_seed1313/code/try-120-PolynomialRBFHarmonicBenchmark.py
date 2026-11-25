import numpy as np

class PolynomialRBFHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Scale input to [-5, 5] domain if needed
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Base polynomial chaos expansion with varying degrees and coefficients
        for i in range(self.dim):
            result += 0.3 * (x[i]**4 + 0.5*x[i]**3 + 0.2*x[i]**2 + 0.1*x[i]) * np.exp(-0.1 * abs(x[i]))
        
        # Add radial basis function components with Gaussian kernels and varying widths
        for i in range(self.dim):
            for j in range(i+1, min(self.dim, i+4)):
                r = np.sqrt((x[i] - x[j])**2 + 0.01)
                result += 0.2 * np.exp(-5.0 * r**2) * (1.0 + 0.1 * i * j)
        
        # Add perturbed harmonic oscillators with frequency modulation and amplitude scaling
        for i in range(self.dim):
            freq = 3.0 + 0.5 * np.sin(0.5 * i)
            result += 0.4 * np.sin(freq * x[i]) * np.cos(freq * x[i] + 0.3 * i) * (1.0 + 0.2 * abs(x[i]))
        
        # Add multi-scale radial components with different frequencies and amplitudes
        if self.dim >= 2:
            r = np.sqrt(x[0]**2 + x[1]**2)
            result += 0.5 * np.sin(8.0 * r) * np.cos(6.0 * r) * np.exp(-0.2 * r**2)
        
        # Add cross-dimensional polynomial interactions with exponential coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * (x[i]**2 + x[j]**2) * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add asymmetric harmonic terms with coordinate-dependent phase shifts
        for i in range(self.dim):
            if x[i] > 0:
                result += 0.3 * np.sin(4.0 * x[i] + 0.5 * x[i]**2) * np.exp(-0.15 * x[i])
            else:
                result += 0.25 * np.cos(3.5 * abs(x[i]) - 0.3 * x[i]) * np.exp(-0.2 * abs(x[i]))
        
        # Add high-frequency chaotic modulation with logistic map-like behavior
        for i in range(self.dim):
            chaos_factor = 0.1 * (np.sin(10.0 * x[i]) + np.cos(7.0 * x[i]))
            result += 0.2 * np.exp(-0.5 * abs(x[i])) * chaos_factor
        
        # Add global polynomial modulation with increasing complexity
        sum_x = np.sum(x)
        result += 0.3 * (sum_x**5 + 0.3*sum_x**4 + 0.1*sum_x**3) * np.exp(-0.1 * abs(sum_x))
        
        # Add boundary attraction and repulsion terms
        for i in range(self.dim):
            result += 0.15 * (5.0 - abs(x[i]))**2 * np.sin(2.0 * x[i])
        
        # Add a small noise component to increase problem difficulty
        noise = 0.05 * np.random.rand()
        result += noise
        
        return result