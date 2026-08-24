import numpy as np

class ChaoticOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with multiple frequencies
        sin_perturbation = np.sum(np.sin(20 * x) * np.cos(7 * x) * np.sin(3 * x))
        
        # Exponential decay terms with different coefficients and higher-order interactions
        exp_decay = np.sum(np.exp(-0.5 * x**2) * np.sin(8 * x) * np.cos(2 * x))
        
        # Chaotic component with nested cubic interactions and cross-dimensional coupling
        chaotic = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaotic += np.sin(x[i] * x[j]**3) * np.cos(x[i]**2 * x[j]) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Add higher-order polynomial terms for increased nonlinearity
        cubic_term = 0.15 * np.sum(x**3)
        quartic_term = 0.05 * np.sum(x**4)
        
        # Add a global scaling factor with modified influence and chaotic modulation
        scaling = 1.0 + 0.2 * np.sum(np.abs(x)) + 0.05 * np.sum(np.sin(10 * x))
        
        # Add a multi-modal component with multiple local minima
        multimodal = 0.3 * np.sum(np.sin(12 * x) * np.cos(4 * x) * np.sin(2 * x))
        
        # Add cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim):
            if i < self.dim - 2:
                coupling += np.exp(-0.1 * (x[i]**2 + x[i+1]**2 + x[i+2]**2)) * np.sin(x[i] * x[i+1] * x[i+2])
        
        return quadratic + 0.7 * sin_perturbation + 0.5 * exp_decay + 0.3 * chaotic + cubic_term + quartic_term + scaling + multimodal + 0.15 * coupling