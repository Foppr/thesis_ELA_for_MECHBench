import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with condition number variation
        f1 = 0.5 * np.sum(x**2)
        
        # Add multiple asymmetric Gaussian peaks with varying heights, widths, and positions
        peaks = []
        for i in range(6):
            mu = np.array([3.0 * np.sin(0.3 * i), 2.0 * np.cos(0.5 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.6 * np.sin(0.8 * i)
            height = 2.0 + 3.0 * np.cos(0.5 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Add saddle point structure with hyperbolic tangent modulation and cross-terms
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(2.0 * x[i] * x[j])
        
        # Introduce gradient variation through fractional exponents and trigonometric modulation
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.7 * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i])
        
        # Add asymmetric basin structure with exponential decay, cosine modulation, and polynomial terms
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.2 * (x[i] - 2.0)**2) * np.cos(0.7 * x[i]) + 0.1 * x[i]**3
        
        # Add cross-terms to increase interaction complexity with higher-order interactions
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.4 * np.sin(x[i] + x[j]) * np.cos(0.7 * x[i] * x[j]) + 0.2 * np.sin(2.0 * x[i] * x[j])
        
        # Add a complex high-dimensional interaction term
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f7 += 0.1 * np.sin(x[i] + x[j] + x[k]) * np.cos(0.3 * x[i] * x[j] * x[k])
        
        # Add noise term to increase robustness
        noise = 0.08 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise