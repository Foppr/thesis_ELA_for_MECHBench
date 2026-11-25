import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced radial component with multiple chaotic frequencies and modulations
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (np.sin(15 * r) + 0.6 * np.sin(30 * r) + 0.4 * np.sin(60 * r) + 
                                 0.2 * np.sin(100 * r))
        
        # Enhanced angular component with higher frequency chaotic interactions
        if self.dim == 1:
            angular = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular = (np.sin(20 * angles) * np.cos(18 * angles) + 
                      0.8 * np.sin(25 * angles) * np.cos(22 * angles) + 
                      0.6 * np.sin(35 * angles) * np.cos(30 * angles) +
                      0.4 * np.sin(45 * angles) * np.cos(40 * angles))
        
        # Enhanced cross-dimensional coupling with multiple interaction types
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_norm[i] - x_norm[j])
                cross += (np.exp(-dist**2) * np.sin(25 * (x_norm[i]**2 + x_norm[j]**2)) * 
                         np.cos(20 * (x_norm[i]**3 + x_norm[j]**3)) +
                         0.5 * np.exp(-dist**3) * np.sin(15 * (x_norm[i]**4 + x_norm[j]**4)) *
                         np.cos(10 * (x_norm[i]**5 + x_norm[j]**5)))
        
        # Enhanced high-frequency chaotic noise component
        noise = np.sum(np.sin(40 * np.pi * x_norm) ** 4 + 
                      0.9 * np.cos(50 * np.pi * x_norm) ** 3 + 
                      0.7 * np.sin(60 * np.pi * x_norm) ** 5 +
                      0.5 * np.cos(70 * np.pi * x_norm) ** 4)
        
        # Enhanced periodic structure with multiple wavelengths and amplitudes
        periodic = (np.sin(3 * np.pi * r) * np.cos(4 * np.pi * r) + 
                   0.6 * np.sin(6 * np.pi * r) * np.cos(8 * np.pi * r) + 
                   0.4 * np.sin(12 * np.pi * r) * np.cos(16 * np.pi * r) +
                   0.2 * np.sin(24 * np.pi * r))
        
        # Enhanced chaotic interaction terms with more complex coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (np.exp(-abs(x_norm[i] - x_norm[j])) * 
                               np.sin(35 * (x_norm[i]**2 + x_norm[j]**2)) * 
                               np.cos(30 * (x_norm[i]**3 + x_norm[j]**3)) +
                               0.6 * np.exp(-abs(x_norm[i] + x_norm[j])) * 
                               np.sin(20 * (x_norm[i]**2 + x_norm[j]**2)) *
                               np.cos(15 * (x_norm[i]**3 + x_norm[j]**3)) +
                               0.3 * np.exp(-(x_norm[i]**2 + x_norm[j]**2)) *
                               np.sin(40 * (x_norm[i]**4 + x_norm[j]**4)))
        
        # Enhanced global conditioning factor with stronger scaling
        cond = 1.0 + 3.0 * np.exp(-self.dim / 4.0)
        
        # Combine all components with increased complexity
        return cond * (radial + angular + cross + noise + periodic + 0.5 * interaction)