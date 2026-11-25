import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute constants for chaotic dynamics
        self.omega = np.random.uniform(0.5, 2.0, dim)
        self.alpha = np.random.uniform(0.1, 0.5, dim)
        self.beta = np.random.uniform(0.3, 1.0, dim)
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Chaotic saddle component with logistic map dynamics
        chaotic = 0.0
        for i in range(self.dim):
            # Logistic map with parameter modulation
            r = 3.8 + 0.2 * np.sin(x_scaled[i] * 2.0)
            chaotic += r * x_scaled[i] * (1.0 - x_scaled[i]) * np.cos(self.omega[i] * x_scaled[i])
        
        # Embedded Gaussian mixture components with varying covariances
        gaussian = 0.0
        for i in range(3):  # Three mixture components
            mu = np.sin(np.linspace(0, 2*np.pi, self.dim) + i*0.5)
            sigma = 0.5 + 0.3 * np.cos(np.arange(self.dim) * 0.7 + i*0.3)
            exp_term = np.sum(((x_scaled - mu) / sigma)**2)
            gaussian += np.exp(-0.5 * exp_term) / (sigma * np.sqrt(2*np.pi)) * (i + 1)
        
        # Polynomial interaction terms with high-order cross-terms
        polynomial = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Higher order interactions with alternating signs
                polynomial += ((x_scaled[i]**3) * (x_scaled[j]**2) * 
                              np.sin(x_scaled[i] + x_scaled[j]) * 
                              np.cos(0.5 * (x_scaled[i] - x_scaled[j])))
        
        # Sharp ridge components with exponential decay
        ridge = 0.0
        for i in range(self.dim):
            # Multiple ridges with different orientations and steepness
            ridge += np.exp(-10.0 * np.abs(x_scaled[i] - np.sin(i*0.3))) * \
                     np.cos(5.0 * x_scaled[i]) * \
                     (1.0 + 0.5 * np.sin(2.0 * x_scaled[i]))
        
        # Cross-term coupling with sinusoidal modulation
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                coupling += (np.sin(x_scaled[i]) * np.cos(x_scaled[j]) * 
                           np.exp(-self.alpha[i] * x_scaled[i]**2) * 
                           np.exp(-self.beta[j] * x_scaled[j]**2))
        
        # Combine all components with carefully tuned weights
        return 0.7 * chaotic + 1.3 * gaussian + 0.8 * polynomial + 0.6 * ridge + 0.5 * coupling