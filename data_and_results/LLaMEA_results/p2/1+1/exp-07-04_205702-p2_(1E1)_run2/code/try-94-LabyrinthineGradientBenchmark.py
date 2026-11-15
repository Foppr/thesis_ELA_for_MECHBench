import numpy as np

class LabyrinthineGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = 0.3 * np.sum(x**2)
        
        # Add multiple elliptic peaks with dynamic scaling and rotation
        f2 = 0.0
        for i in range(6):
            angle = 0.5 * i * np.pi / 3.0
            cos_a, sin_a = np.cos(angle), np.sin(angle)
            rot_x = x[0] * cos_a - x[1] * sin_a
            rot_y = x[0] * sin_a + x[1] * cos_a
            sigma_x = 0.5 + 0.5 * np.sin(0.3 * i)
            sigma_y = 0.5 + 0.5 * np.cos(0.3 * i)
            height = 2.0 + 3.0 * np.sin(0.4 * i)
            f2 -= height * np.exp(-0.5 * ((rot_x / sigma_x)**2 + (rot_y / sigma_y)**2))
        
        # Add labyrinthine structure using periodic functions
        f3 = 0.0
        for i in range(self.dim):
            f3 += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Introduce dynamic gradient modulation with time-like parameter
        f4 = 0.0
        for i in range(self.dim):
            f4 += (np.abs(x[i])**1.7) * np.sin(3.0 * x[i] + 0.5 * i)
        
        # Add terrain roughness with multiple interacting sinusoidal components
        f5 = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                f5 += 0.2 * np.sin(x[i] + x[j]) * np.cos(0.5 * x[i] * x[j]) * np.exp(-0.05 * (x[i] - x[j])**2)
        
        # Add basin asymmetry through exponential and trigonometric combinations
        f6 = 0.0
        for i in range(self.dim):
            f6 += np.exp(-0.2 * (x[i] - 2.0)**2) * np.sin(1.2 * x[i]) * np.cos(0.8 * x[i])
        
        # Add cross-term interactions with varying weights
        f7 = 0.0
        weights = np.linspace(0.1, 0.8, self.dim)
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = weights[i] * weights[j]
                f7 += weight * np.tanh(x[i] + x[j]) * np.sin(0.7 * x[i] * x[j])
        
        # Add noise for robustness
        noise = 0.03 * np.random.rand()
        
        # Combine all components
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + noise