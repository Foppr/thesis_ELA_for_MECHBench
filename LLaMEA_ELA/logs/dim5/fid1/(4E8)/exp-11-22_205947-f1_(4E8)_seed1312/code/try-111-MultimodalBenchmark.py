import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree and stronger coupling
        polynomial = 1.2 * np.sum(x**2) + 0.3 * np.sum(x**3) + 0.05 * np.sum(x**4) + 0.01 * np.sum(x**5) + 0.002 * np.sum(x**6)
        
        # Stronger chaotic trigonometric interactions with increased frequency modulation
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Extended coupling range
                trigonometric += (np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) + 
                                np.cos(5.0 * x[i]) * np.sin(6.0 * x[j]) +
                                np.sin(2.0 * x[i]) * np.sin(7.0 * x[j]) +
                                np.cos(3.5 * x[i]) * np.cos(5.5 * x[j]) +
                                np.sin(4.5 * x[i]) * np.cos(2.5 * x[j]))
        
        # Modified radial basis functions with dynamic centers and widths
        rbfs = 0.0
        centers = np.linspace(-4.8, 4.8, min(9, self.dim))
        for i, center in enumerate(centers):
            if len(centers) <= self.dim:
                width = 0.1 + 0.2 * np.sin(i * 0.7)  # Dynamic varying widths
                rbfs += np.exp(-0.5 * np.sum(((x - center) / width)**2)) * (1.0 + 0.2 * np.sin(i * 1.2))
        
        # Complex correlation term with higher-order interactions and non-linear coupling
        correlation = 0.0
        for i in range(self.dim - 3):
            correlation += (x[i] - x[i+1])**3 * np.sin(5.0 * x[i]) + \
                          (x[i] - x[i+2])**3 * np.cos(4.0 * x[i+1]) + \
                          (x[i] - x[i+3])**2 * np.tan(3.5 * x[i+2]) + \
                          (x[i] - x[i+1])**2 * np.exp(-0.5 * (x[i+2] - x[i+3])**2)
        
        # Multi-modal component with increased harmonic complexity
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.6 * np.sin(8.0 * x[i]) * np.cos(9.0 * x[i]) + \
                         0.4 * np.sin(13.0 * x[i]) * np.cos(12.0 * x[i]) + \
                         0.2 * np.tanh(5.0 * x[i]) * np.log(1.0 + np.abs(x[i])) + \
                         0.1 * np.sin(15.0 * x[i]) * np.cos(14.0 * x[i])
        
        # Enhanced chaotic sine component with double phase modulation
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.3 * np.sin(20.0 * x[i] + np.sin(8.0 * x[i]) * np.cos(9.0 * x[i]) + 
                                   np.cos(10.0 * x[i]) * np.sin(7.0 * x[i]))
        
        # Quaternion-inspired hybrid term with multi-scale coupling
        quaternion = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                quaternion += (np.sin(x[i]) * np.cos(x[i+1]) + 
                              np.cos(x[i]) * np.sin(x[i+1])) * \
                             np.exp(-0.1 * (x[i]**2 + x[i+1]**2)) * \
                             np.sin(3.0 * x[i] + 2.0 * x[i+1])
        
        # Adaptive scaling factor with enhanced modulation
        adaptive_scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.7) + 0.05 * np.cos(self.dim * 0.3)
        
        return adaptive_scale * (polynomial + 0.4 * trigonometric + 0.2 * rbfs + 0.15 * correlation + 0.25 * multimodal + 0.15 * chaotic + 0.1 * quaternion)