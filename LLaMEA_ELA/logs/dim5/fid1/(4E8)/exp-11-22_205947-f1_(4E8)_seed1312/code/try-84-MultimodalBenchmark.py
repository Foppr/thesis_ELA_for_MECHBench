import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree, cross-dimensional interactions, and exponential scaling
        polynomial = np.sum(x**2) + 0.3 * np.sum(x**3) + 0.05 * np.sum(x**4) + 0.01 * np.sum(x**5) + 0.005 * np.sum(np.exp(0.1 * np.abs(x)))
        
        # Dynamic sinusoidal coupling with varying frequencies, phase shifts, and dimensionality-dependent modulation
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range
                freq_i = 2.0 + 0.5 * np.sin(i * 0.8)
                freq_j = 3.0 + 0.4 * np.cos(j * 0.6)
                trigonometric += (np.sin(freq_i * x[i]) * np.cos(freq_j * x[j]) + 
                                np.cos(freq_i * x[i]) * np.sin(freq_j * x[j]) +
                                np.sin(freq_i * x[i] + freq_j * x[j]) * np.cos(freq_i * x[i] - freq_j * x[j]))
        
        # Enhanced radial basis function with multiple centers, varying widths, adaptive scaling, and exponential decay
        rbfs = 0.0
        centers = np.linspace(-4.9, 4.9, min(11, self.dim))
        for i, center in enumerate(centers):
            if len(centers) <= self.dim:
                width = 0.2 + 0.15 * np.sin(i * 0.6)  # Varying widths
                rbfs += np.exp(-0.3 * np.sum(((x - center) / width)**2)) * (1.0 + 0.3 * np.sin(i * 0.5)) * np.exp(-0.05 * i)
        
        # Stronger correlation term with higher-order interactions, adaptive coupling, and chaotic modulation
        correlation = 0.0
        for i in range(self.dim - 4):
            coupling_factor = 1.0 + 0.2 * np.sin(i * 0.7)  # Adaptive coupling
            correlation += coupling_factor * ((x[i] - x[i+1])**2 * np.sin(6.0 * x[i]) + \
                          (x[i] - x[i+2])**2 * np.cos(5.0 * x[i+1]) + \
                          (x[i] - x[i+3])**2 * np.tan(4.0 * x[i+2]) + \
                          (x[i] - x[i+4])**2 * np.exp(-0.1 * x[i+3]**2))
        
        # Multi-modal component with multiple local minima, sigmoidal modulations, and exponential interactions
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.7 * np.sin(9.0 * x[i]) * np.cos(10.0 * x[i]) + \
                         0.5 * np.sin(14.0 * x[i]) * np.cos(13.0 * x[i]) + \
                         0.3 * np.tanh(6.0 * x[i]) * np.log(1.0 + np.abs(x[i])) + \
                         0.2 * np.exp(-0.5 * x[i]**2) * np.sin(15.0 * x[i])
        
        # Chaotic sine component with dynamic phase modulation and exponential scaling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.4 * np.sin(20.0 * x[i] + np.sin(9.0 * x[i]) * np.cos(10.0 * x[i])) * np.exp(-0.02 * i)
        
        # Quaternion-inspired hybrid term with complex multi-dimensional coupling and dynamic scaling
        quaternion = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                scale_factor = 1.0 + 0.1 * np.sin(i * 0.5)
                quaternion += (np.sin(x[i]) * np.cos(x[i+1]) + 
                              np.cos(x[i]) * np.sin(x[i+1])) * \
                             np.exp(-0.15 * (x[i]**2 + x[i+1]**2)) * scale_factor
        
        # Adaptive scaling factor with dimension-dependent complexity, dynamic modulation, and exponential component
        adaptive_scale = 1.0 + 0.2 * np.log(self.dim + 1) + 0.15 * np.sin(self.dim * 0.7) + 0.08 * np.cos(self.dim * 0.3) + 0.05 * np.exp(-0.01 * self.dim)
        
        return adaptive_scale * (polynomial + 0.5 * trigonometric + 0.25 * rbfs + 0.2 * correlation + 0.3 * multimodal + 0.2 * chaotic + 0.15 * quaternion)