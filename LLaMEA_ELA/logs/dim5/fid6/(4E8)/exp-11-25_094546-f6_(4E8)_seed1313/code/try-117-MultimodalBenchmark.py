import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Enhanced hyperchaotic fractal component with modified nesting and scaling
        fractal = 0.0
        for i in range(self.dim):
            xi = x_norm[i]
            scale = 1.0
            nested_sum = 0.0
            for k in range(1, 10):  # Reduced nesting to 9 levels
                scale *= 0.4  # Slightly increased scaling factor
                nested_sum += scale * np.sin(2**(k+2) * xi + k * np.pi/5)
            fractal += nested_sum
        
        # Enhanced time-delayed feedback with modified quantum-like phase interactions
        feedback = 0.0
        for i in range(self.dim):
            if i > 2:
                delay = x_norm[i-1] + 0.4 * x_norm[i-2] - 0.3 * x_norm[i-3]
                # Modified quantum phase interference
                phase = np.exp(1j * (8.0 * delay + 0.6 * i))
                feedback += np.real(phase * np.exp(-0.35 * delay**2))
            else:
                feedback += np.sin(9.0 * x_norm[i]) * np.exp(-0.35 * x_norm[i]**2)
        
        # Advanced adaptive landscape erosion with modified roughness
        erosion = 0.0
        for i in range(self.dim):
            erosion_rate = 0.25 + 0.45 * np.sin(3.5 * x_norm[i]) + 0.35 * np.cos(2.5 * i)
            erosion += erosion_rate * (x_norm[i]**5 - 3.0 * x_norm[i]**3 + 1.5 * x_norm[i])
        
        # Quantum-inspired interference patterns with altered frequency modulation
        interference = 0.0
        for i in range(self.dim):
            freq_base = 2.0**(i % 4 + 3)  # Reduced base frequency variation
            # Modified tunneling effect
            tunneling = np.exp(-0.45 * (x_norm[i] - 0.4)**2)
            interference += tunneling * np.sin(freq_base * x_norm[i]) * np.cos(freq_base * x_norm[i] * 1.3)
        
        # Enhanced cross-dimensional coupling with modified entanglement effects
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Reduced coupling range to 4 dimensions
                dist = np.abs(x_norm[i] - x_norm[j])
                # Modified entanglement strength
                entanglement = 0.75 + 0.25 * np.sin(0.6 * (i + j))
                strength = entanglement * np.exp(-dist**2 * (2.5 + 0.4 * (i+j)))
                cross += strength * np.sin(18.0 * dist) * np.cos(7.0 * dist)
        
        # Quantum-inspired dynamic scaling with modified dimensionality modulation
        dynamic_scale = 1.0 + 0.7 * np.sin(self.dim * 0.45) * np.cos(np.mean(x_norm)**2.5)
        
        # Combined components with adjusted weights for improved balance and challenge
        weight_fractal = 0.43 + 0.06 * np.sin(self.dim * 0.35)
        weight_feedback = 0.32 + 0.14 * np.cos(self.dim * 0.2)
        weight_erosion = 0.23 + 0.13 * np.tanh(self.dim * 0.12)
        weight_interference = 0.19 + 0.05 * np.sin(self.dim * 0.18)
        weight_cross = 0.16  # Slightly increased cross-weight for enhanced challenge
        
        return dynamic_scale * (weight_fractal * fractal + 
                               weight_feedback * feedback + 
                               weight_erosion * erosion + 
                               weight_interference * interference + 
                               weight_cross * cross)