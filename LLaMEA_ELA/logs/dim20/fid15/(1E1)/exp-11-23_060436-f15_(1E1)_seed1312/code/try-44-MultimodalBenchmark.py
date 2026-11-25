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
            # Slightly modified frequencies and amplitudes
            multimodal += (np.sin(1.5*x[i]) * np.cos(2.5*x[i]) * np.exp(-((x[i] - np.pi)**2 / 4.0)) +
                          np.sin(1.8*x[i]) * np.cos(4.2*x[i]) * np.exp(-((x[i] + np.pi)**2 / 12.0)) +
                          np.sin(0.7*x[i]) * np.cos(6.8*x[i]) * np.exp(-((x[i] - 2*np.pi)**2 / 9.0)) +
                          np.sin(3.5*x[i]) * np.cos(1.5*x[i]) * np.exp(-((x[i] - 2.5)**2 / 7.0)))
            
        # Add a more complex chaotic component with exponential scaling and cross-terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(x[i] * np.exp(-0.5*x[i]**2)) * np.cos(x[i] * np.exp(-0.3*x[i]**2)) * 
                       np.exp(-((x[i] - 1.2)**2 / 2.5)) + 
                       np.sin(0.8*x[i] * np.cos(x[i])) * np.cos(1.2*x[i] * np.sin(x[i])) * 
                       np.exp(-((x[i] + 1.8)**2 / 5.5)))
            
        # Add a polynomial component with higher-order terms and interaction terms
        poly = 0
        for i in range(self.dim):
            poly += (x[i]**6 - 12*x[i]**4 + 40*x[i]**2) * np.exp(-((x[i] - 1.8)**2 / 1.5))
            
        # Add interaction terms between dimensions to increase complexity
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (np.sin(1.2*x[i]) * np.cos(0.8*x[j]) * np.exp(-((x[i] - x[j])**2 / 4.0)) +
                               np.cos(0.9*x[i]) * np.sin(1.1*x[j]) * np.exp(-((x[i] + x[j])**2 / 8.0)))
        
        # Combine all components with varying weights and scaling factors
        return sphere * 0.03 + multimodal * 0.37 + chaotic * 0.28 + poly * 0.22 + interaction * 0.1