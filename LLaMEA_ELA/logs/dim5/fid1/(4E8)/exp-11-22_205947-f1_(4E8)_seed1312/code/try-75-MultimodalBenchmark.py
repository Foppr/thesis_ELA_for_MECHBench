import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher degree interactions and cross-dimensional coupling
        polynomial = np.sum(x**2) + 0.2 * np.sum(x**3) + 0.03 * np.sum(x**4) + 0.008 * np.sum(x**5)
        
        # Complex trigonometric interactions with multiple frequencies, coupled dimensions, and chaotic sine terms
        trigonometric = 0.0
        for i in range(self.dim):
            for j in range(max(0, i-3), min(i+4, self.dim)):  # Sparse coupling for complexity control
                if i != j:
                    trigonometric += (np.sin(3.0 * x[i]) * np.cos(4.0 * x[j]) + 
                                    np.cos(5.0 * x[i]) * np.sin(6.0 * x[j]) +
                                    np.sin(2.0 * x[i]) * np.sin(7.0 * x[j]) +
                                    0.1 * np.sin(10.0 * x[i] + np.sin(5.0 * x[j])))  # Chaotic coupling
        
        # Enhanced radial basis function with multiple centers, varying widths, and non-uniform distribution
        rbfs = 0.0
        centers = np.linspace(-4.0, 4.0, min(9, self.dim))
        for i, center in enumerate(centers):
            if len(centers) <= self.dim:
                width = 0.3 + 0.15 * np.sin(i * 0.7)  # Varying widths
                rbfs += np.exp(-0.3 * np.sum(((x - center) / width)**2))
        
        # Stronger correlation term with higher-order interactions and chaotic components
        correlation = 0.0
        for i in range(self.dim - 2):
            correlation += (x[i] - x[i+1])**2 * np.sin(5.0 * x[i]) + \
                          (x[i] - x[i+2])**2 * np.cos(4.0 * x[i+1]) + \
                          0.05 * np.sin(8.0 * x[i]) * np.cos(6.0 * x[i+1])  # Additional chaotic interaction
        
        # Multi-modal component with enhanced local optima and irregular distribution
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += 0.6 * np.sin(8.0 * x[i]) * np.cos(9.0 * x[i]) + \
                         0.4 * np.sin(15.0 * x[i]) * np.cos(14.0 * x[i]) + \
                         0.2 * np.sin(20.0 * x[i]) * np.cos(19.0 * x[i])
        
        # Additional chaotic sine component with dynamic frequency modulation
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += 0.3 * np.sin(20.0 * x[i] + np.sin(10.0 * x[i]) + np.sin(5.0 * x[i]))
        
        # Adaptive scaling factor with dimension-dependent complexity and dynamic modulation
        adaptive_scale = 1.2 + 0.15 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * 0.3) + 0.08 * np.cos(self.dim * 0.7)
        
        return adaptive_scale * (polynomial + 0.4 * trigonometric + 0.2 * rbfs + 0.15 * correlation + 0.25 * multimodal + 0.15 * chaotic)