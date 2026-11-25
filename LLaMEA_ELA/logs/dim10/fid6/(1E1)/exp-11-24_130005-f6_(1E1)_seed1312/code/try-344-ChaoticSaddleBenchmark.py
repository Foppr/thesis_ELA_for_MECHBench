import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic component with sine-cosine mix and varying frequencies
        chaotic = 0.0
        for i in range(self.dim):
            freq = 2.0 + 1.5 * np.sin(x_scaled[i] * 0.5)
            amp = 1.0 + 0.5 * np.cos(x_scaled[i] * 0.3)
            chaotic += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 1.2)
        
        # Periodic orbit embedding with multiple stable fixed points
        periodic = 0.0
        for i in range(self.dim):
            # Embedded periodic orbits at specific locations
            orbit1 = np.sin(x_scaled[i] * 2.0) ** 2
            orbit2 = np.cos(x_scaled[i] * 3.0) ** 2
            orbit3 = np.sin(x_scaled[i] * 5.0) ** 2
            periodic += 0.5 * orbit1 + 0.3 * orbit2 + 0.2 * orbit3
        
        # Saddle point structure with hyperbolic tangent transitions
        saddle = 0.0
        for i in range(self.dim):
            # Hyperbolic tangent based transition regions creating saddle behavior
            tanh_term = np.tanh(5.0 * x_scaled[i])
            saddle += tanh_term ** 2 * (1.0 - tanh_term ** 2)
        
        # Multi-scale interference pattern with exponential decay
        interference = 0.0
        for scale in [1, 2, 3]:
            for i in range(self.dim):
                interference += np.sin(scale * x_scaled[i]) * \
                              np.cos(scale * x_scaled[i] * 0.7) * \
                              np.exp(-scale * np.abs(x_scaled[i]))
        
        # Cross-term interactions with phase shifts creating complex valleys
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                cross += np.sin(x_scaled[i] + x_scaled[j]) * \
                        np.cos(x_scaled[i] - x_scaled[j]) * \
                        np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combine all components with adaptive weights
        return 1.2 * chaotic + 0.8 * periodic + 0.6 * saddle + 0.5 * interference + 0.4 * cross