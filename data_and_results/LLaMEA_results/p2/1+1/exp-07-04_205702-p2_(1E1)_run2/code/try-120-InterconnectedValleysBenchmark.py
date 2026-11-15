import numpy as np

class InterconnectedValleysBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.3 * np.sum(x**2)
        
        # Add multiple interconnected valley structures with varying depths
        valleys = []
        for i in range(3):
            mu = np.array([2.5 * np.sin(0.8 * i), 2.0 * np.cos(0.6 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            depth = 1.0 + 1.5 * np.sin(0.5 * i)
            width = 0.5 + 0.8 * np.cos(0.4 * i)
            valley = depth * np.exp(-0.5 * np.sum(((x - mu) / width)**2))
            valleys.append(valley)
        
        f2 = np.sum(valleys)
        
        # Add ridge structures with varying heights and orientations
        ridges = []
        for i in range(2):
            mu = np.array([3.0 * np.sin(0.7 * i), 1.5 * np.cos(0.5 * i)] + [0.0] * (self.dim - 2))[:self.dim]
            height = 0.8 + 1.2 * np.sin(0.6 * i)
            width = 0.3 + 0.6 * np.cos(0.3 * i)
            ridge = height * np.exp(-0.5 * np.sum(((x - mu) / width)**2))
            ridges.append(ridge)
        
        f3 = np.sum(ridges)
        
        # Introduce directional bias through sinusoidal modulation
        f4 = 0.0
        for i in range(self.dim):
            f4 += np.sin(1.2 * x[i]) * np.cos(0.8 * x[(i+1) % self.dim]) * (1.0 + 0.5 * np.sin(0.3 * x[i]))
        
        # Add curvature variation through polynomial terms
        f5 = 0.0
        for i in range(self.dim):
            f5 += 0.1 * x[i]**4 + 0.2 * x[i]**3 - 0.1 * x[i]**2
        
        # Create asymmetric basin structure with logarithmic decay
        f6 = 0.0
        for i in range(self.dim):
            f6 -= 0.5 * np.log(1.0 + 0.1 * (x[i] - 2.0)**2) * np.sin(0.5 * x[i])
        
        # Add cross-terms to increase interaction complexity
        f7 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f7 += 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) * (x[i] + x[j])**2
        
        # Add noise term to increase robustness
        noise = 0.03 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise