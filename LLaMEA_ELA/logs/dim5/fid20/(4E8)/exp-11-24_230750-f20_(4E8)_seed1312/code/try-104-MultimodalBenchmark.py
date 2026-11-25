import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like curvature with recursive scaling
        fractal = 0.0
        for i in range(self.dim):
            scaled_x = x[i] * (1.0 + 0.1 * np.sin(i * np.pi / 4))
            fractal += np.abs(scaled_x) ** (1.5 + 0.3 * np.sin(i * 0.7))
        
        # Quantum tunneling effect with complex phase interactions
        quantum = 0.0
        for i in range(self.dim):
            phase = np.exp(1j * x[i] * (1.0 + 0.2 * np.cos(i * 0.5)))
            quantum += np.real(phase * np.conj(phase))
        
        # Dynamic basin transitions with time-dependent parameters
        basin = 0.0
        for i in range(self.dim):
            t_param = 0.5 * np.sin(self.dim * 0.3 + i * 0.1)
            basin += (x[i] - t_param)**2 * np.cos(x[i]**2) * np.exp(-0.1 * np.abs(x[i]))
        
        # Chaotic gradient modulation with modified logistic map
        chaotic = 0.0
        r = 3.9 + 0.15 * np.sin(self.dim * 0.25)  # Slightly increased chaos parameter
        for i in range(self.dim):
            logistic = (r * np.abs(x[i]) * (1 - np.abs(x[i]))) if np.abs(x[i]) < 1 else 0
            chaotic += logistic * np.sin(i * 0.4 + x[i] + 0.1 * np.sin(x[i]))  # Added sine coupling
        
        # Multi-scale ridge structure with varying widths
        ridge = 0.0
        for i in range(min(3, self.dim)):
            width = 0.5 + 0.3 * np.sin(i * 0.6)
            ridge += np.exp(-0.5 * ((x[i] - 1.0) / width)**2) + np.exp(-0.5 * ((x[i] + 1.0) / width)**2)
        
        # Asymmetric basin penalty with exponential decay
        penalty = 0.0
        for i in range(self.dim):
            if x[i] > 2.0:
                penalty += 2.0 * np.exp(-0.5 * (x[i] - 2.0)**2)
            elif x[i] < -2.0:
                penalty += 2.0 * np.exp(-0.5 * (x[i] + 2.0)**2)
        
        # Add novel hyperbolic sine coupling term for enhanced multimodality
        sinh_coupling = 0.0
        for i in range(self.dim):
            sinh_coupling += np.sinh(x[i] * (1.0 + 0.05 * np.cos(i * 0.8)))
        
        # Combine all components with dimension-adaptive weights
        weights = [1.0 + 0.2 * np.sin(i * 0.3) for i in range(self.dim)]
        result = 0.0
        for i in range(self.dim):
            result += weights[i] * (fractal + basin + chaotic + ridge)
        
        # Add quantum interference term
        interference = 0.1 * np.sin(np.sum(x)**2)
        
        # Add small random noise for robustness
        noise = 0.005 * np.random.rand()
        
        return result + penalty + interference + noise + 0.3 * sinh_coupling