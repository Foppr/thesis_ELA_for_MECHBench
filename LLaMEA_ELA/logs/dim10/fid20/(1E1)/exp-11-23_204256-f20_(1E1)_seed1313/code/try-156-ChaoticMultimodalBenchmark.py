import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple sinusoidal frequencies and exponential decay
        r = np.sqrt(np.sum(x_norm**2))
        radial = np.exp(-r**2) * (np.sin(10 * r) + 0.5 * np.sin(25 * r) + 0.3 * np.sin(50 * r))
        
        # Angular component with chaotic behavior using sine and cosine products
        if self.dim == 1:
            angular = 0
        else:
            angles = np.arctan2(x_norm[1], x_norm[0])
            angular = (np.sin(15 * angles) * np.cos(12 * angles) + 
                      0.7 * np.sin(22 * angles) * np.cos(18 * angles) + 
                      0.4 * np.sin(35 * angles) * np.cos(27 * angles))
        
        # Cross-dimensional coupling with chaotic exponential interactions
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = abs(x_norm[i] - x_norm[j])
                cross += np.exp(-dist**2) * np.sin(20 * (x_norm[i]**2 + x_norm[j]**2)) * \
                        np.cos(15 * (x_norm[i]**3 + x_norm[j]**3))
        
        # High-frequency chaotic noise component
        noise = np.sum(np.sin(30 * np.pi * x_norm) ** 4 + 
                      0.8 * np.cos(40 * np.pi * x_norm) ** 3 + 
                      0.6 * np.sin(50 * np.pi * x_norm) ** 5)
        
        # Periodic structure with multiple wavelengths
        periodic = (np.sin(2 * np.pi * r) * np.cos(3 * np.pi * r) + 
                   0.5 * np.sin(4 * np.pi * r) * np.cos(6 * np.pi * r) + 
                   0.3 * np.sin(8 * np.pi * r))
        
        # Chaotic interaction terms with varying coupling strengths
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (np.exp(-abs(x_norm[i] - x_norm[j])) * 
                               np.sin(30 * (x_norm[i]**2 + x_norm[j]**2)) * 
                               np.cos(25 * (x_norm[i]**3 + x_norm[j]**3)) + 
                               0.5 * np.exp(-abs(x_norm[i] + x_norm[j])) * 
                               np.sin(15 * (x_norm[i]**2 + x_norm[j]**2)))
        
        # Global conditioning factor with exponential scaling
        cond = 1.0 + 2.0 * np.exp(-self.dim / 3.0)
        
        # Combine all components
        return cond * (radial + angular + cross + noise + periodic + 0.4 * interaction)