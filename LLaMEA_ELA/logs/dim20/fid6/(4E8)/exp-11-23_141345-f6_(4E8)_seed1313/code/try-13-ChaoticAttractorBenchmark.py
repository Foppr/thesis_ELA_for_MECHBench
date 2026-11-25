import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute attractor positions for different dimensions
        if dim == 2:
            # Cross-shaped attractors at specific points
            self.attractors = np.array([
                [0.0, 0.0],     # Center
                [3.0, 0.0],     # Right
                [-3.0, 0.0],    # Left
                [0.0, 3.0],     # Top
                [0.0, -3.0]     # Bottom
            ])
        elif dim == 3:
            # 3D cross-shaped attractors
            self.attractors = np.array([
                [0.0, 0.0, 0.0],
                [3.0, 0.0, 0.0],
                [-3.0, 0.0, 0.0],
                [0.0, 3.0, 0.0],
                [0.0, -3.0, 0.0],
                [0.0, 0.0, 3.0],
                [0.0, 0.0, -3.0]
            ])
        else:
            # High-dimensional cross-shaped attractors
            self.attractors = np.zeros((dim * 2 + 1, dim))
            for i in range(dim):
                self.attractors[2*i+1, i] = 3.0
                self.attractors[2*i+2, i] = -3.0
            self.attractors[0] = np.zeros(dim)

    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term with chaotic sinusoidal modulation
        radial_term = np.sum(x**2) * 0.01
        sinusoidal_mod = np.sin(np.sum(x**2) * 0.5) * 0.3
        
        # Cross-shaped attractor term
        attractor_term = 0.0
        for attractor in self.attractors:
            dist = np.sum((x - attractor)**2)
            # Use a combination of Gaussian and inverse distance weighting
            gaussian_weight = np.exp(-dist / 2.0) * 0.5
            inverse_weight = 1.0 / (dist + 0.1)
            attractor_term += gaussian_weight * inverse_weight
        
        # Chaotic component with multiple frequency sinusoids
        chaotic_component = 0.0
        for i in range(self.dim):
            chaotic_component += np.sin(x[i] * (i + 1) * 2.0) * np.cos(x[i] * (i + 1) * 1.5)
        
        # Combine all terms with different scaling factors
        result = radial_term + sinusoidal_mod + attractor_term + chaotic_component * 0.1
        
        return result