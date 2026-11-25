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
            for k in range(1, 15):  # Increased nesting to 14 levels
                scale *= 0.32  # Further reduced scaling factor
                nested_sum += scale * np.sin(2**(k+4) * xi + k * np.pi/5)
            fractal += nested_sum
        
        # Enhanced time-delayed feedback with quantum-like phase interactions
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                delay = x_norm[i-1] + 0.4 * x_norm[i-2] - 0.3 * x_norm[i-3]
                # Quantum phase interference added with modified coefficients
                phase = np.exp(1j * (12.0 * delay + 0.6 * i))
                feedback += np.real(phase * np.exp(-0.5 * delay**2))
            else:
                feedback += np.sin(12.0 * x_norm[i]) * np.exp(-0.5 * x_norm[i]**2)
        
        # Advanced adaptive landscape erosion with fractal roughness
        erosion = 0.0
        for i in range(self.dim):
            erosion_rate = 0.25 + 0.6 * np.sin(4.5 * x_norm[i]) + 0.35 * np.cos(3.5 * i)
            erosion += erosion_rate * (x_norm[i]**5 - 3.5 * x_norm[i]**3 + 1.7 * x_norm[i])
        
        # Quantum-inspired interference patterns with dynamic frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 6 + 3)  # Increased base frequency variation
            # Added quantum tunneling effect with different parameters
            tunneling = np.exp(-0.4 * (x_norm[i] - 0.4)**2)
            interference += tunneling * np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.5)
        
        # Enhanced cross-dimensional coupling with quantum entanglement effects
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Increased coupling range to 6 dimensions
                dist = np.abs(x_norm[i] - x_norm[j])
                # Quantum entanglement strength with different modulation
                entanglement = 0.75 + 0.25 * np.sin(0.6 * (i + j))
                strength = entanglement * np.exp(-dist**2 * (3.5 + 0.6 * (i+j)))
                cross += strength * np.sin(22.0 * dist) * np.cos(9.0 * dist)
        
        # Quantum-inspired dynamic scaling with dimensionality-dependent modulation
        dynamic_scale = 1.0 + 0.9 * np.sin(self.dim * 0.6) * np.cos(np.mean(x_norm)**4)
        
        # Combined components with adjusted weights for improved balance and challenge
        weight_fractal = 0.45 + 0.08 * np.sin(self.dim * 0.35)
        weight_feedback = 0.28 + 0.16 * np.cos(self.dim * 0.3)
        weight_erosion = 0.26 + 0.13 * np.tanh(self.dim * 0.12)
        weight_interference = 0.19 + 0.07 * np.sin(self.dim * 0.25)
        weight_cross = 0.17  # Slightly increased cross-weight for enhanced challenge
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)