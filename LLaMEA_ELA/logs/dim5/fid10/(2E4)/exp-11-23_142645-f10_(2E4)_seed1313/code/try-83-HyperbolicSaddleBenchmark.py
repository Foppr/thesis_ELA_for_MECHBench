import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Hyperbolic tangent interaction terms with position-dependent coupling
        tanh_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                coupling = 0.3 + 0.2 * np.tanh(0.5 * (x[i] + x[j]))
                tanh_interaction += coupling * np.tanh(dist) * np.cos(2.0 * (x[i] - x[j]))
        
        # Polynomial coupling terms with varying degrees and coefficients
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                degree = 2 + int((i + j) % 3)
                coeff = 0.5 + 0.3 * np.sin(i * 0.8) * np.cos(j * 0.6)
                poly_coupling += coeff * (dist ** degree) * np.sin(1.5 * (x[i] + x[j]))
        
        # Dynamic saddle-point clustering with position-dependent weights
        saddle_cluster = 0.0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.7 * x[i])
            saddle_cluster += weight * np.tanh(2.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Adaptive conditioning with exponential and logarithmic scaling
        condition = np.sum(np.exp(0.2 * np.abs(x)) * np.log(1.0 + 0.1 * np.abs(x)))
        
        # Multi-scale oscillatory component with frequency modulation
        oscillatory = np.sum(np.sin(4.0 * x) * np.cos(2.5 * x) * np.exp(-0.1 * x**2))
        
        # Asymmetric basin structure with piecewise polynomial terms
        basin_structure = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                basin_structure += 0.3 * x[i]**3 + 0.2 * x[i]**2
            else:
                basin_structure += 0.2 * x[i]**4 - 0.1 * x[i]**2
        
        # Combined fitness value with dynamic weighting based on component dominance
        total = 0.25 * tanh_interaction + 0.2 * poly_coupling + 0.15 * saddle_cluster + 0.2 * condition + 0.15 * oscillatory + 0.05 * basin_structure
        
        return total