import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum-like interference terms with phase modulation and amplitude scaling
        quantum_terms = np.sum(np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x) * np.exp(-0.1 * np.abs(x)))
        
        # Saddle-point attractor components with dynamic positioning and stability control
        saddle_terms = 0.0
        for i in range(min(4, self.dim)):
            pos = np.sin(i * np.pi / 3) * 3.0
            stability = 1.0 + 0.5 * np.cos(i * 0.8)
            saddle_terms += stability * (x[i] - pos)**2 * np.cos(5 * (x[i] - pos))
        
        # Adaptive penalty landscape with dimensionality-dependent scaling and non-linear transformation
        penalty = 0.0
        for i in range(self.dim):
            penalty += (1.0 + 0.3 * np.sin(i * 0.5)) * np.exp(0.5 * (x[i] / 4.0)**2) * (1.0 + 0.2 * np.abs(x[i]))
        
        # Enhanced polynomial cross-terms with asymmetric coupling and higher-order interactions
        poly_cross = 0.0
        for i in range(self.dim - 1):
            poly_cross += (x[i]**3 + x[i+1]**3) * np.sin(0.5 * (x[i] + x[i+1])) * (1.0 + 0.1 * np.abs(x[i]))
        
        # Rugged terrain with fractal-like characteristics and multi-scale irregularities
        rugged = 0.0
        for i in range(self.dim):
            rugged += np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * (x[i]**2))
        
        # Memory-dependent dynamics through delayed feedback and temporal correlation
        memory = 0.0
        for i in range(1, min(5, self.dim)):
            memory += 0.3 * x[i] * x[i-1] * np.sin(0.2 * (x[i] - x[i-1]))
        
        # Novel hyperbolic tangent coupling with variable coupling strength and directional bias
        tanh_coupling = 0.0
        for i in range(self.dim - 2):
            tanh_coupling += np.tanh(x[i] + x[i+1]) * np.tanh(x[i+1] + x[i+2]) * (1.0 + 0.25 * np.abs(x[i]))
        
        # Add noise with chaotic modulation and directional correlation
        noise = 0.2 * np.random.rand() * np.sum(np.sin(15 * x) * np.cos(9 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combined function value
        return quantum_terms + saddle_terms + penalty + poly_cross + rugged + memory + tanh_coupling + noise