import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree interactions
        polynomial = np.sum(x**2) + 0.15 * np.sum(x**3) + 0.02 * np.sum(x**4) + 0.005 * np.sum(x**5)
        
        # Complex trigonometric interactions with multiple frequencies and coupled dimensions
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                trigonometric += (np.sin(2.5 * x[i]) * np.cos(3.5 * x[j]) + 
                                np.cos(4.5 * x[i]) * np.sin(5.5 * x[j]) +
                                np.sin(1.5 * x[i]) * np.sin(6.0 * x[j]))
        
        # Enhanced radial basis function with multiple centers and varying widths
        rbfs = 0.0
        centers = np.linspace(-4.5, 4.5, min(7, self.dim))
        for i, center in enumerate(centers):
            if len(centers) <= self.dim:
                width = 0.5 + 0.2 * np.sin(i)  # Varying widths
                rbfs += np.exp(-0.5 * np.sum(((x - center) / width)**2))
        
        # Stronger correlation term with higher-order interactions
        correlation = 0.0
        for i in range(self.dim - 2):
            correlation += (x[i] - x[i+1])**2 * np.sin(4.0 * x[i]) + \
                          (x[i] - x[i+2])**2 * np.cos(3.0 * x[i+1])
        
        # Additional multi-modal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.5 * np.sin(7.0 * x[i]) * np.cos(8.0 * x[i]) + \
                         0.3 * np.sin(12.0 * x[i]) * np.cos(11.0 * x[i])
        
        # Chaotic sine component for increased complexity
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.2 * np.sin(15.0 * x[i] + np.sin(7.0 * x[i]))
        
        # Adaptive scaling factor with dimension-dependent complexity
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1) + 0.05 * np.sin(self.dim * 0.5)
        
        return adaptive_scale * (polynomial + 0.3 * trigonometric + 0.15 * rbfs + 0.1 * correlation + 0.2 * multimodal + 0.1 * chaotic)