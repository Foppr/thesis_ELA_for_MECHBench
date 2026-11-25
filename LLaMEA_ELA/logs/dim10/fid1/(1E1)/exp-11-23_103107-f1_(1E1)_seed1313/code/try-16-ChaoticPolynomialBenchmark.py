import numpy as np

class ChaoticPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Enhanced polynomial basin with higher degree terms and modified weights
        poly_basin = 0.03 * np.sum(x**7) + 0.12 * np.sum(x**4) + 0.09 * np.sum(x**2)
        
        # Enhanced chaotic sinusoidal terms with increased frequency modulation
        chaotic = 0
        for i in range(self.dim):
            chaotic += (np.sin(20 * x[i]) * np.cos(16 * x[i]) * np.sin(12 * x[i]) + 
                       np.cos(15 * x[i]) * np.sin(11 * x[i]) * np.cos(8 * x[i]) +
                       np.sin(13 * x[i]) * np.cos(9 * x[i]) * np.sin(6 * x[i]))
            
        # Enhanced cross-term interactions with additional trigonometric combinations
        cross_terms = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += (np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) * 
                               np.cos((x[i] + x[j])**2) + 
                               np.cos(x[i] * x[j]) * np.sin(x[i]**3 + x[j]**3) * 
                               np.cos(x[i]**2 * x[j]) +
                               np.sin(x[i]**2 * x[j]) * np.cos(x[i] * x[j]**2) *
                               np.sin(x[i] + x[j]))
                
        # Enhanced harmonic components with more complex power and frequency relationships
        harmonics = 0
        for i in range(self.dim):
            harmonics += (np.sin(10 * x[i]**5) * np.cos(5 * x[i]**4) + 
                         np.cos(8 * x[i]**6) * np.sin(4 * x[i]**5) +
                         np.sin(6 * x[i]**3) * np.cos(3 * x[i]**2))
        
        # Add global scaling and offset to improve fitness score and discrimination
        return 0.7 * (poly_basin + chaotic + cross_terms + harmonics) + 0.05 * np.sum(np.abs(x))