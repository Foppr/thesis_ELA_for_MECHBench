import numpy as np

class QuantumSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like recursive structure with self-similar patterns
        fractal_term = 0.0
        for i in range(self.dim):
            term = x[i] ** 4
            for k in range(1, 6):
                term += 0.2 * np.sin(k * x[i]) * np.cos(k * x[i]) * (x[i] ** (3 + k % 3))
            fractal_term += term
        
        # Adaptive saddle-point conditioning with position-dependent curvature
        saddle_condition = 0.0
        for i in range(self.dim):
            # Saddle point behavior with varying curvature
            curvature = 1.0 + 0.3 * np.sin(0.4 * x[i]) * np.cos(0.6 * x[i])
            saddle_condition += curvature * (x[i] ** 2) * np.exp(-0.1 * x[i]**2)
        
        # Quantum-inspired interference patterns with complex amplitude modulation
        quantum_interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.01)
                phase = np.sin(2.0 * dist) + 0.5 * np.cos(3.0 * dist)
                amplitude = 1.0 + 0.4 * np.sin(0.7 * x[i]) * np.cos(0.9 * x[j])
                quantum_interference += amplitude * np.sin(phase * dist) * np.exp(-0.05 * dist**2)
        
        # Multi-scale oscillatory landscape with dynamic frequency adjustment
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.cos(0.3 * x[i])
            oscillatory += freq * np.sin(freq * x[i]) * np.exp(-0.2 * np.abs(x[i]))
        
        # Asymmetric basin with piecewise hyperbolic and polynomial components
        asymmetric_basin = 0.0
        for i in range(self.dim):
            if x[i] < 0:
                asymmetric_basin += 0.5 * np.tanh(0.5 * x[i]) + 0.2 * x[i]**3
            else:
                asymmetric_basin += 0.3 * np.cosh(0.4 * x[i]) - 0.1 * x[i]**2
        
        # Cross-term coupling with quantum-like phase interference
        cross_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                phase_diff = np.sin(0.5 * (x[i] + x[j])) * np.cos(0.3 * (x[i] - x[j]))
                weight = 1.0 + 0.3 * np.sin(x[i]) * np.cos(x[j])
                cross_coupling += weight * phase_diff * (x[i]**2 + x[j]**2) * np.exp(-0.1 * np.abs(x[i] - x[j]))
        
        # Combined fitness value with dynamic weighting
        total = 0.25 * fractal_term + 0.2 * saddle_condition + 0.25 * quantum_interference + 0.15 * oscillatory + 0.1 * asymmetric_basin + 0.05 * cross_coupling
        
        return total