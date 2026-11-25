import numpy as np

class SaddleRidgeFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base quadratic term with elliptical distortion
        result = 0.5 * np.sum(x**2) + 0.1 * np.sum(x**4)
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 2.0 * (i + 1)
            amp = 2.0 / (i + 1)**1.5
            result += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.5)
            
        # Cross-dimensional coupling with adaptive strengths and saddle-point interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((i - j)**2 + 1.0)
                strength = 1.0 / (dist**1.2 + 1.0)
                freq = 2.5 * dist
                result += strength * np.sin(freq * x[i]) * np.cos(freq * x[j])
                
        # Ridge and valley structures with exponential decay
        ridge_valley = 0.0
        for i in range(self.dim):
            ridge_valley += np.exp(-0.2 * x[i]**2) * np.sin(5.0 * x[i]) + 0.3 * np.cos(8.0 * x[i])
        result += 0.5 * ridge_valley
        
        # Saddle-point enhancing terms with higher-order polynomial interactions
        for i in range(self.dim):
            result += 0.1 * (x[i]**3) * np.sin(3.0 * x[i]) + 0.05 * (x[i]**5)
            
        # Additional global perturbation with multiple frequency components
        global_pert = 0.0
        for i in range(self.dim):
            global_pert += 0.2 * np.sin(10.0 * x[i]) + 0.15 * np.cos(15.0 * x[i]) + 0.1 * np.sin(20.0 * x[i])
        result += global_pert
        
        # Convergence term with exponential decay and enhanced nonlinearity
        result += 0.2 * np.exp(-0.3 * np.sum(x**2)) + 0.15 * np.exp(-0.6 * np.sum(x**4))
        
        return result