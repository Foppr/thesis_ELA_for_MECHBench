import numpy as np

class ChaoticTentBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize chaotic parameters for each dimension
        self.omega = np.random.uniform(0.1, 0.9, dim)
        self.alpha = np.random.uniform(0.5, 2.0, dim)
        self.beta = np.random.uniform(0.1, 1.0, dim)
        
    def f(self, x):
        # Scale input to [0, 1] range
        x_scaled = (x + 5.0) / 10.0
        
        # Chaotic tent map component with bifurcation points
        chaotic = 0.0
        for i in range(self.dim):
            # Tent map with parameterized omega and alpha
            xi = x_scaled[i]
            if xi < self.omega[i]:
                value = self.alpha[i] * xi
            else:
                value = self.alpha[i] * (1 - xi)
            chaotic += np.sin(value * np.pi) * np.cos(value * 2 * np.pi)
        
        # Cross-dimensional coupling with nonlinear interaction terms
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                # Nonlinear coupling between dimensions with varying strength
                coupling_strength = 0.5 + 0.5 * np.sin((i + j) * 0.5)
                coupling += coupling_strength * np.sin(x_scaled[i] * x_scaled[j]) * \
                           np.exp(-np.abs(x_scaled[i] - x_scaled[j]))
        
        # Multi-scale periodic component with varying frequencies
        periodic = 0.0
        for scale in [1, 2, 3, 4]:
            for i in range(self.dim):
                freq = scale * (1 + 0.5 * np.sin(i * 0.7))
                periodic += np.sin(freq * x_scaled[i]) * \
                           np.cos(freq * x_scaled[i] * 0.8) * \
                           np.exp(-scale * x_scaled[i]**2)
        
        # Bifurcation point attraction with varying beta parameters
        attraction = 0.0
        for i in range(self.dim):
            # Attraction to multiple bifurcation points
            point1 = 0.3 + 0.1 * np.sin(i * 0.5)
            point2 = 0.7 + 0.1 * np.cos(i * 0.3)
            dist1 = np.abs(x_scaled[i] - point1)
            dist2 = np.abs(x_scaled[i] - point2)
            attraction += self.beta[i] * (np.exp(-dist1**2) + np.exp(-dist2**2))
        
        # Combine all components with adaptive weights
        return 0.8 * chaotic + 1.2 * coupling + 0.6 * periodic + 0.9 * attraction