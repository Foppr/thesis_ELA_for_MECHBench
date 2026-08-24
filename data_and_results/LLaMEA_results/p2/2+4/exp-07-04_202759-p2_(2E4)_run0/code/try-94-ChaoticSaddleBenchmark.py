import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute rotation matrices for adaptive layers
        self.rotations = []
        for i in range(4):
            angle = np.random.rand() * 2 * np.pi
            c, s = np.cos(angle), np.sin(angle)
            self.rotations.append(np.array([[c, -s], [s, c]]))
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Saddle-point component with chaotic perturbations
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x[i]**2 - 1.0)**2 + 0.1 * np.sin(10 * x[i]) * np.cos(5 * x[i])
        
        # Gaussian mixture component with adaptive weights and positions
        gaussian = 0.0
        centers = np.linspace(-4.0, 4.0, min(8, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            weight = 2.0 + 0.5 * np.sin(0.7 * i)
            sigma = 0.5 + 0.2 * np.cos(0.9 * i)
            gaussian += weight * np.exp(-0.5 * ((x[i] - center) / sigma)**2)
        
        # Adaptive rotation layer with chaotic modulation
        rot_layer = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                # Apply rotation
                vec = np.array([x[i], x[i+1]])
                rot = self.rotations[i % len(self.rotations)]
                rotated = rot @ vec
                # Add chaotic modulation
                mod = 1.0 + 0.3 * np.sin(3 * np.sum(vec))
                rot_layer += mod * (rotated[0]**3 + rotated[1]**3)
        
        # Embedded sinusoidal coupling with multi-scale frequencies
        coupling = 0.0
        for i in range(self.dim):
            freqs = [1.0, 2.0, 5.0, 10.0]
            for f in freqs:
                coupling += np.sin(f * x[i]) * np.cos(f * x[i] * 0.5) * np.exp(-0.1 * x[i]**2)
        
        # Memory-like term with exponential decay
        memory = 0.0
        for i in range(1, self.dim):
            memory += np.exp(-0.2 * (x[i] - x[i-1])**2) * np.sin(5 * (x[i] + x[i-1]))
        
        # Combine components with dynamic scaling
        return 0.3 * saddle + 0.25 * gaussian + 0.2 * rot_layer + 0.15 * coupling + 0.1 * memory