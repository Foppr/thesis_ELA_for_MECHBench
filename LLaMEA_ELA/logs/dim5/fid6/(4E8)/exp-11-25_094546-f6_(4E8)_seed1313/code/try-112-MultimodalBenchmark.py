import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperchaotic fractal component with increased nesting and complexity
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 12):  # Increased nesting to 11 levels
                scale *= 0.35  # Further reduced scaling factor
                nested_sum += scale * np.sin(2**(k+3) * xi + k * np.pi/4)
            fractal += nested_sum
        
        # Enhanced time-delayed feedback with quantum-like phase interactions
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                delay = x_norm[i-1] + 0.5 * x_norm[i-2] - 0.2 * x_norm[i-3]
                # Quantum phase interference added
                phase = np.exp(1j * (10.0 * delay + 0.5 * i))
                feedback += np.real(phase * np.exp(-0.4 * delay**2))
            else:
                feedback += np.sin(10.0 * x_norm[i]) * np.exp(-0.4 * x_norm[i]**2)
        
        # Advanced adaptive landscape erosion with fractal roughness
        erosion = 0.0
        for i in range(self.dim):
            erosion_rate = 0.2 + 0.5 * np.sin(4.0 * x_norm[i]) + 0.3 * np.cos(3.0 * i)
            erosion += erosion_rate * (x_norm[i]**5 - 3.0 * x_norm[i]**3 + 1.5 * x_norm[i])
        
        # Quantum-inspired interference patterns with dynamic frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 5 + 2)  # Increased base frequency variation
            # Added quantum tunneling effect
            tunneling = np.exp(-0.5 * (x_norm[i] - 0.5)**2)
            interference += tunneling * np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.4)
        
        # Enhanced cross-dimensional coupling with quantum entanglement effects
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling range to 5 dimensions
                dist = np.abs(x_norm[i] - x_norm[j])
                # Quantum entanglement strength
                entanglement = 0.8 + 0.2 * np.sin(0.5 * (i + j))
                strength = entanglement * np.exp(-dist**2 * (3.0 + 0.5 * (i+j)))
                cross += strength * np.sin(20.0 * dist) * np.cos(8.0 * dist)
        
        # Quantum-inspired dynamic scaling with dimensionality-dependent modulation
        dynamic_scale = 1.0 + 0.8 * np.sin(self.dim * 0.5) * np.cos(np.mean(x_norm)**3)
        
        # Combined components with adjusted weights for improved balance and challenge
        weight_fractal = 0.42 + 0.07 * np.sin(self.dim * 0.4)
        weight_feedback = 0.31 + 0.15 * np.cos(self.dim * 0.25)
        weight_erosion = 0.24 + 0.14 * np.tanh(self.dim * 0.1)
        weight_interference = 0.18 + 0.06 * np.sin(self.dim * 0.2)
        weight_cross = 0.15  # Increased cross-weight for enhanced challenge
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)