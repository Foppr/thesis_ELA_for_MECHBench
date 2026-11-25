import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree and cross-dimensional interactions
        polynomial = np.sum(x**2) + 0.2 * np.sum(x**3) + 0.03 * np.sum(x**4) + 0.008 * np.sum(x**5)
        
        # Complex trigonometric interactions with multiple frequencies and stronger coupling
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range
                trigonometric += (np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) + 
                                np.cos(5.0 * x[i]) * np.sin(6.0 * x[j]) +
                                np.sin(2.0 * x[i]) * np.sin(7.0 * x[j]) +
                                np.cos(3.5 * x[i]) * np.cos(5.5 * x[j]))
        
        # Enhanced radial basis function with multiple centers and varying widths
        rbfs = 0.0
        centers = np.linspace(-4.0, 4.0, min(9, self.dim))
        for i, center in enumerate(centers):
            if len(centers) <= self.dim:
                width = 0.6 + 0.15 * np.sin(i * 0.7)  # Varying widths with different phase
                rbfs += np.exp(-0.5 * np.sum(((x - center) / width)**2))
        
        # Stronger correlation term with higher-order interactions and adaptive weights
        correlation = 0.0
        for i in range(self.dim - 3):
            correlation += (x[i] - x[i+1])**2 * np.sin(5.0 * x[i]) + \
                          (x[i] - x[i+2])**2 * np.cos(4.0 * x[i+1]) + \
                          (x[i] - x[i+3])**2 * np.sin(3.0 * x[i+2])
        
        # Additional multi-modal component with multiple local minima and varying amplitudes
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.6 * np.sin(8.0 * x[i]) * np.cos(9.0 * x[i]) + \
                         0.4 * np.sin(13.0 * x[i]) * np.cos(12.0 * x[i]) + \
                         0.2 * np.sin(18.0 * x[i]) * np.cos(17.0 * x[i])
        
        # Chaotic sine component with increased complexity and dynamic coupling
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.25 * np.sin(18.0 * x[i] + np.sin(8.0 * x[i]) + np.cos(6.0 * x[i]))
        
        # Adaptive scaling factor with enhanced dimension-dependent complexity and dynamic adjustments
        adaptive_scale = 1.0 + 0.15 * np.log(self.dim + 1) + 0.08 * np.sin(self.dim * 0.7) + 0.03 * np.cos(self.dim * 0.4)
        
        return adaptive_scale * (polynomial + 0.35 * trigonometric + 0.2 * rbfs + 0.15 * correlation + 0.25 * multimodal + 0.15 * chaotic)