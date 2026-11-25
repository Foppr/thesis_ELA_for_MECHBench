import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with chaotic behavior
        multimodal = 0
        for i in range(self.dim):
            # Create multiple local minima using sinusoidal functions with varying frequencies
            multimodal += (np.sin(x[i]) * np.cos(3*x[i]) * np.exp(-((x[i] - np.pi)**2 / 5.0)) +
                          np.sin(2*x[i]) * np.cos(5*x[i]) * np.exp(-((x[i] + np.pi)**2 / 15.0)) +
                          np.sin(0.5*x[i]) * np.cos(7*x[i]) * np.exp(-((x[i] - 2*np.pi)**2 / 10.0)))
            
        # Add a chaotic component with exponential scaling
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.sin(x[i] * np.exp(-x[i]**2)) * np.cos(x[i] * np.exp(-x[i]**2)) * np.exp(-((x[i] - 1.0)**2 / 3.0))
            
        # Add a polynomial component for additional complexity
        poly = 0
        for i in range(self.dim):
            poly += (x[i]**4 - 6*x[i]**2 + 8*x[i]) * np.exp(-((x[i] - 1.5)**2 / 2.0))
        
        # Add a new component: Gaussian mixture with varying centers and variances
        gaussian_mixture = 0
        centers = [0, 1.5, -1.5, 3.0, -3.0]
        for i in range(self.dim):
            for center in centers:
                gaussian_mixture += np.exp(-((x[i] - center)**2 / 0.5)) * np.sin(x[i] * np.pi)
        
        # Combine all components with varying weights and scaling factors
        return sphere * 0.05 + multimodal * 0.35 + chaotic * 0.25 + poly * 0.2 + gaussian_mixture * 0.15