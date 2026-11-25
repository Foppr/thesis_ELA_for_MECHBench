import numpy as np

class HyperbolicSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced hyperbolic tangent interaction terms with modified coupling
        tanh_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                coupling = 0.4 + 0.3 * np.tanh(0.6 * (x[i] + x[j]))
                tanh_interaction += coupling * np.tanh(1.5 * dist) * np.cos(2.5 * (x[i] - x[j]))
        
        # Modified polynomial coupling terms with different degrees and coefficients
        poly_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                degree = 3 + int((i + j) % 4)
                coeff = 0.6 + 0.4 * np.sin(i * 0.9) * np.cos(j * 0.7)
                poly_coupling += coeff * (dist ** degree) * np.sin(2.0 * (x[i] + x[j]))
        
        # Dynamic saddle-point clustering with modified weights
        saddle_cluster = 0.0
        for i in range(self.dim):
            weight = 1.2 + 0.6 * np.sin(0.8 * x[i])
            saddle_cluster += weight * np.tanh(2.5 * x[i]) * np.cos(3.5 * x[i])
        
        # Adaptive conditioning with modified exponential and logarithmic scaling
        condition = np.sum(np.exp(0.3 * np.abs(x)) * np.log(1.0 + 0.15 * np.abs(x)))
        
        # Multi-scale oscillatory component with frequency modulation
        oscillatory = np.sum(np.sin(5.0 * x) * np.cos(3.0 * x) * np.exp(-0.15 * x**2))
        
        # Asymmetric basin structure with piecewise polynomial terms
        basin_structure = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                basin_structure += 0.4 * x[i]**3 + 0.3 * x[i]**2
            else:
                basin_structure += 0.3 * x[i]**4 - 0.2 * x[i]**2
        
        # Combined fitness value with dynamic weighting based on component dominance
        total = 0.3 * tanh_interaction + 0.25 * poly_coupling + 0.18 * saddle_cluster + 0.18 * condition + 0.12 * oscillatory + 0.07 * basin_structure
        
        return total