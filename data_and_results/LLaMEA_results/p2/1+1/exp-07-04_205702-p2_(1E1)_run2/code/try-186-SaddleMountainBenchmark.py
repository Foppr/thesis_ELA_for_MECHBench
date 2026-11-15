import numpy as np

class SaddleMountainBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.5 * np.sum(x**2)
        
        # Add multiple asymmetric Gaussian peaks with varying heights and widths
        peaks = []
        for i in range(6):
            mu = np.array([2.0 * np.sin(0.5 * i), 3.0 * np.cos(0.3 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            sigma = 0.2 + 0.6 * np.sin(0.7 * i)
            height = 1.0 + 3.0 * np.cos(0.4 * i)
            peak = height * np.exp(-0.5 * np.sum(((x - mu) / sigma)**2))
            peaks.append(peak)
        
        f2 = np.sum(peaks)
        
        # Add saddle point structure with hyperbolic tangent modulation and chaotic sine
        f3 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f3 += np.tanh(x[i]) * np.tanh(x[j]) * np.sin(1.5 * x[i] * x[j] + 0.3 * np.sin(2.0 * x[i]))
        
        # Introduce gradient variation through fractional exponents and chaotic modulation
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.abs(x[i])**1.7 * np.sin(2.5 * x[i] + 0.5 * np.cos(3.0 * x[i]))
        
        # Add asymmetric basin structure with exponential decay and cosine modulation
        f5 = 0.0
        for i in range(self.dim):
            f5 -= np.exp(-0.15 * (x[i] - 1.5)**2) * np.cos(0.6 * x[i] + 0.2 * np.sin(1.5 * x[i]))
        
        # Add cross-terms to increase interaction complexity with chaotic modulation
        f6 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f6 += 0.3 * np.sin(x[i] + x[j] + 0.1 * np.sin(x[i] * x[j])) * np.cos(0.5 * x[i] * x[j] + 0.2 * np.cos(x[i] + x[j]))
        
        # Add a new component to improve robustness and challenge with higher-order terms
        f7 = 0.0
        for i in range(self.dim):
            f7 += 0.2 * np.sin(3.0 * x[i]) * np.cos(0.5 * x[i]**2 + 0.1 * np.sin(x[i]**3))
        
        # Add a new component to increase multimodality and complexity with polynomial chaos
        f8 = 0.0
        for i in range(self.dim):
            f8 += 0.1 * np.sin(0.5 * x[i]) * np.exp(-0.1 * x[i]**2) * np.cos(0.3 * x[i]**3)
        
        # Add dynamic noise term to increase robustness
        noise = 0.03 * np.random.rand() * (1.0 + 0.5 * np.sin(np.sum(x)))
        
        # Add higher-order polynomial interactions for increased complexity
        f9 = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                for k in range(j+1, self.dim):
                    f9 += 0.05 * x[i]**2 * x[j] * x[k] * np.sin(0.1 * x[i] + 0.2 * x[j] + 0.3 * x[k])
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9 + noise