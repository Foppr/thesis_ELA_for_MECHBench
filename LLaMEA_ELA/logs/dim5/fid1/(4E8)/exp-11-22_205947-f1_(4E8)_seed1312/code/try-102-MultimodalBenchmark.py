import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with modified weights and higher degree interactions
        polynomial = 0.8 * np.sum(x**2) + 0.15 * np.sum(x**3) + 0.02 * np.sum(x**4) + 0.005 * np.sum(x**5)
        
        # Modified trigonometric interactions with altered frequencies and coupling
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling range
                trigonometric += (np.sin(2.5 * x[i]) * np.cos(3.5 * x[j]) + 
                                np.cos(4.5 * x[i]) * np.sin(5.5 * x[j]) +
                                np.sin(1.5 * x[i]) * np.sin(6.5 * x[j]) +
                                np.cos(3.0 * x[i]) * np.cos(4.0 * x[j]))
        
        # Radial basis function with modified centers and widths
        rbfs = 0.0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i, center in enumerate(centers):
            if len(centers) <= self.dim:
                width = 0.2 + 0.15 * np.sin(i * 0.8)  # Different varying widths
                rbfs += np.exp(-0.5 * np.sum(((x - center) / width)**2)) * (1.0 + 0.15 * np.sin(i))
        
        # Correlation term with different interaction patterns
        correlation = 0.0
        for i in range(self.dim - 2):
            correlation += (x[i] - x[i+1])**2 * np.sin(4.0 * x[i]) + \
                          (x[i] - x[i+2])**2 * np.cos(3.0 * x[i+1]) + \
                          (x[i] - x[i+1])**2 * np.tan(2.5 * x[i+2])
        
        # Multi-modal component with altered frequencies and sigmoidal modulations
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.5 * np.sin(7.0 * x[i]) * np.cos(8.0 * x[i]) + \
                         0.3 * np.sin(12.0 * x[i]) * np.cos(11.0 * x[i]) + \
                         0.1 * np.tanh(4.0 * x[i]) * np.log(1.0 + np.abs(x[i]))
        
        # Chaotic sine component with modified phase modulation
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.25 * np.sin(15.0 * x[i] + np.sin(7.0 * x[i]) * np.cos(8.0 * x[i]))
        
        # Quaternion-inspired hybrid term with different coupling
        quaternion = 0.0
        for i in range(0, self.dim - 1, 2):
            if i + 1 < self.dim:
                quaternion += (np.sin(x[i]) * np.cos(x[i+1]) + 
                              np.cos(x[i]) * np.sin(x[i+1])) * \
                             np.exp(-0.08 * (x[i]**2 + x[i+1]**2))
        
        # Adaptive scaling factor with different modulation
        adaptive_scale = 1.0 + 0.12 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * 0.6) + 0.03 * np.cos(self.dim * 0.25)
        
        return adaptive_scale * (polynomial + 0.35 * trigonometric + 0.18 * rbfs + 0.12 * correlation + 0.22 * multimodal + 0.13 * chaotic + 0.08 * quaternion)