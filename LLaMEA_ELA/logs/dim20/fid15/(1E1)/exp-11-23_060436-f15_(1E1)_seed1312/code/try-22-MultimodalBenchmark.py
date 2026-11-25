import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with enhanced chaotic behavior
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima using sinusoidal functions with varying frequencies and amplitudes
            multimodal += (np.sin(x[i]) * np.cos(3*x[i]) * np.exp(-((x[i] - np.pi)**2 / 5.0)) +
                          np.sin(2*x[i]) * np.cos(5*x[i]) * np.exp(-((x[i] + np.pi)**2 / 15.0)) +
                          np.sin(0.5*x[i]) * np.cos(7*x[i]) * np.exp(-((x[i] - 2*np.pi)**2 / 10.0)) +
                          np.sin(4*x[i]) * np.cos(2*x[i]) * np.exp(-((x[i] - 3.0)**2 / 8.0)))
            
        # Add a more complex chaotic component with exponential scaling and cross-terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(x[i] * np.exp(-x[i]**2)) * np.cos(x[i] * np.exp(-x[i]**2)) * 
                       np.exp(-((x[i] - 1.0)**2 / 3.0)) + 
                       np.sin(x[i] * np.cos(x[i])) * np.cos(x[i] * np.sin(x[i])) * 
                       np.exp(-((x[i] + 2.0)**2 / 6.0)))
            
        # Add a polynomial component with higher-order terms and interaction terms
        poly = 0
        for i in range(self.dim):
            poly += (x[i]**5 - 10*x[i]**3 + 30*x[i]) * np.exp(-((x[i] - 1.5)**2 / 2.0))
            
        # Add interaction terms between dimensions to increase complexity
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (np.sin(x[i]) * np.cos(x[j]) * np.exp(-((x[i] - x[j])**2 / 5.0)) +
                               np.cos(x[i]) * np.sin(x[j]) * np.exp(-((x[i] + x[j])**2 / 10.0)))
        
        # Add a new component: Gaussian mixture with varying centers and variances
        gaussian_mixture = 0
        centers = [0, 1, -1, 2, -2]
        for i in range(self.dim):
            for center in centers:
                gaussian_mixture += np.exp(-((x[i] - center)**2 / 0.5)) * np.sin(x[i])
        
        # Combine all components with optimized weights and scaling factors
        return sphere * 0.03 + multimodal * 0.30 + chaotic * 0.25 + poly * 0.15 + interaction * 0.15 + gaussian_mixture * 0.12